# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from address.models import AddressField, Country, State, Locality, Address
from django.forms import ModelForm
from django import forms
from django.utils.text import slugify
from agenda.models import WeekTemplate, DayTemplate, Slot
from timezone_field import TimeZoneField
from django.core.validators import RegexValidator
import os
from dateutil.relativedelta import relativedelta
from datetime import datetime
from utils.toolbox import string_random
import requests


class ColorSlot(models.Model):
    SLOT_TYPE = settings.SLOT_TYPE
    slot = models.IntegerField(verbose_name=_(u'Type of slot'), choices=SLOT_TYPE)
    free_slot_color = models.CharField(verbose_name=_(u'Free pricing free slot color'), default='#73B5EB', max_length=8)
    booked_slot_color = models.CharField(verbose_name=_(u'Booked slot color'), default='#F64636', max_length=8)

    def __str__(self):
        return ' %d - %d' % (self.id, self.slot)


class TypePrice(models.Model):
    type = models.IntegerField(verbose_name=_(u'note paid'), choices=settings.TYPE_OFFER)
    price_exVAT = models.IntegerField(verbose_name=_(u'exVAT price'))
    num_months = models.IntegerField(verbose_name=_(u'Number of months'))
    auto_extension = models.BooleanField(verbose_name=_('Auto Extension'), default=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    def get_typename(self):
        for t in settings.TYPE_OFFER:
            if t[0] == self.type:
                return t[1]

    def __str__(self):
        return u"%s %s" % (self.get_typename(), self.info())

    def unicode(self):
        return u"%s %s" % (self.get_typename(), self.info())

    def info(self):
        ret = u'(%d %s) : %d euros ' % (
            self.num_months, _(u'month') if self.num_months < 2 else _(u'months'), self.price_exVAT)
        ret += u'%s' % _(u'excl. VAT')
        return ret


class InvoiceNumber(models.Model):
    year = models.IntegerField(verbose_name=_(u'Year'), default=2015)
    number = models.IntegerField(verbose_name=_(u'Number'), default=0)

    def __str__(self):
        return u"%s" % self.year


def get_number(y):
    inst = InvoiceNumber.objects.filter(year=y)
    if len(inst):
        inst[0].number += 1
        inst[0].save()
        val = inst[0].number
    else:
        inst = InvoiceNumber(year=y, number=1)
        inst.save()
        val = 1
    val += (y * 10 ** 7) + (67 * 10 ** 5)
    return val


class Invoice(models.Model):
    type_price = models.ForeignKey(TypePrice, verbose_name=_(u'Type of subscription'), blank=False)
    date_creation = models.DateField(verbose_name=_(u'Creation date'), auto_now_add=True)
    date_start = models.DateField(verbose_name=_(u'Start date'), blank=False)
    date_end = models.DateField(verbose_name=_(u'End date'), blank=False)
    active = models.BooleanField(verbose_name=_(u'Active'), default=False)
    price_exVAT = models.FloatField(verbose_name=_(u'Price excl. VAT'), blank=False, default=0.0)
    VAT = models.FloatField(verbose_name=_(u'VAT (%)'), blank=False, default=21)
    price_VAT = models.FloatField(verbose_name=_(u'Price VAT'), blank=True, default=0.0)
    price_incVAT = models.FloatField(verbose_name=_(u'Price inc. VAT'), blank=True, default=0.0)
    paid = models.BooleanField(verbose_name=_(u'Paid'), default=False)
    date_paid = models.DateField(verbose_name=_(u'date paid'), blank=True, null=True)
    note_paid = models.CharField(verbose_name=_(u'note paid'), max_length=100, blank=True)
    show = models.BooleanField(verbose_name=_(u'Show'), default=True)
    invoice_number = models.IntegerField(blank=True, default=0)
    path = models.CharField(verbose_name=_(u'path'), max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.date_start:
            self.date_start = datetime.now()
        self.date_end = self.date_start + relativedelta(months=+self.type_price.num_months)
        super(Invoice, self).save(*args, **kwargs)
        if self.price_incVAT != ((self.VAT / 100) * self.price_exVAT) + self.price_exVAT:
            self.price_VAT = (self.VAT / 100) * self.price_exVAT
            self.price_incVAT = self.price_VAT + self.price_exVAT
            # super(Invoice, self).save(*args, **kwargs)
        self.invoice_number = get_number(self.date_creation.year)
        self.path = os.path.join('invoice',
                                 '%s_%s_%s.pdf' % (string_random(16), self.date_creation.year, self.invoice_number))
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return '%d: %s' % (self.id, self.type_price)


class MiniInvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['type_price']

    def __init__(self, *args, **kwargs):
        super(MiniInvoiceForm, self).__init__(*args, **kwargs)
        self.fields['type_price'].queryset = TypePrice.objects.filter(active=True)
        self.fields['type_price'].widget.attrs['class'] = 'select2'
        self.fields['type_price'].widget.attrs['style'] = 'width:100%'


class NoFreeMiniInvoiceForm(MiniInvoiceForm):
    def __init__(self, *args, **kwargs):
        super(MiniInvoiceForm, self).__init__(*args, **kwargs)
        self.fields['type_price'].queryset = TypePrice.objects.filter(active=True).exclude(price_exVAT=0)
        self.fields['type_price'].widget.attrs['class'] = 'select2'
        self.fields['type_price'].widget.attrs['style'] = 'width:100%'


class Doctor(models.Model):
    MEDECINE_CHOICES = settings.MEDECINE_CHOICES
    TITLE_CHOICES = settings.TITLE_CHOICES

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")

    title = models.IntegerField(verbose_name=_(u'Title'), choices=TITLE_CHOICES)
    picture = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH, blank=True, null=True)
    speciality = models.IntegerField(verbose_name=_(u'Speciality'), choices=MEDECINE_CHOICES)
    slug = models.SlugField(verbose_name=_(u'slug'), max_length=50, blank=True)

    vat_number = models.CharField(verbose_name=_(u'VAT number'), max_length=20, blank=True)
    telephone = models.CharField(verbose_name=_(u'Telephone'), validators=[phone_regex],
                                 help_text=_(u'format : +32475123456'), max_length=20, blank=True)
    address = AddressField()
    start_time = models.TimeField(verbose_name=_(u'Start time'), blank=False, default="09:00")
    end_time = models.TimeField(verbose_name=_(u'End time'), blank=False, default="18:00")
    colorslots = models.ManyToManyField(ColorSlot, verbose_name=_(u'ColorSlot'), blank=True)
    view_busy_slot = models.BooleanField(verbose_name=_(u'Can see busy slots'), default=True)
    view_in_list = models.BooleanField(verbose_name=_(u'Can see in doctors list'), default=True)
    weektemplate = models.ForeignKey(WeekTemplate, verbose_name=_(u'Week template'), blank=True, null=True)
    slots = models.ManyToManyField(Slot, verbose_name=_(u'Slots'), blank=True)
    confirm = models.TextField(verbose_name=_(u'Confirm key'), blank=True, null=True)
    text_rdv = models.TextField(verbose_name=_(u'Text RDV'), blank=True, null=True)
    text_horaires = models.TextField(verbose_name=_(u'Text horaires'), blank=True, null=True)
    timezone = TimeZoneField(default=settings.TIME_ZONE)
    invoices = models.ManyToManyField(Invoice, verbose_name=_(u'Invoices'), blank=True)
    can_recharge = models.BooleanField(verbose_name=_(u'Can recharge type of subscription '), blank=False, null=False,
                                       default=True)
    refer_userprofile = models.ForeignKey('users.UserProfile', verbose_name=_('UserProfile'),
                                          related_name='refer_userprofile', null=True, blank=True)

    def __str__(self):
        return u"%s " % self.slug

    def get_title(self):
        return u"%s" % self.TITLE_CHOICES[self.title - 1][1]

    def get_speciality(self):
        return u"%s" % self.MEDECINE_CHOICES[self.speciality - 1][1]

    def full_name(self):
        return u"%s %s" % (self.get_title(), self.real_name())

    def real_name(self):
        if self.refer_userprofile is not None:
            return u"%s %s" % (self.refer_userprofile.user.first_name, self.refer_userprofile.user.last_name)
        else:
            return None

    def get_n_colorslots(self):
        return len(self.colorslots.all())

    def get_colorslot(self, i):
        ret = None
        if self.get_n_colorslots() > 0:
            for cs in self.colorslots.all():
                if cs.slot == i:
                    ret = cs
        if ret is None:
            ret = ColorSlot(slot=i, free_slot_color=settings.SLOT_COLOR[i - 1])
            ret.save()
            self.colorslots.add(ret)
            self.save()
        return ret

    def set_slug(self):
        if not self.slug:
            if self.refer_userprofile is not None:
                self.slug = slugify(self.real_name())

    def get_all_slottemplates(self):
        out = []
        if len(self.get_weektemplate().days.all()) > 0:
            for dt in self.get_weektemplate().days.all():
                for s in dt.slots.all():
                    out.append(s.as_json(dt.day, self))
        return out

    def remove_all_slottemplates(self):
        self.get_weektemplate().remove_all_slottemplates()

    def get_weektemplate(self):
        if not self.weektemplate:
            wk = WeekTemplate()
            wk.save()
            self.weektemplate = wk
            self.save()
        return self.weektemplate

    def get_daytemplate(self, i):
        return self.get_weektemplate().get_daytemplate(i)

    def get_color(self, i, booked):
        slot = self.get_colorslot(i)
        return str(slot.booked_slot_color) if booked else str(slot.free_slot_color)

    def get_active_invoice(self):
        if len(self.invoices.all()):
            for i in self.invoices.filter(active=True):
                if i.active:
                    return i
        else:
            return None

    def already_use_free_invoice(self):
        out = False
        if len(self.invoices.all()):
            for i in self.invoices.all():
                if i.price_exVAT == 0:
                    out = True
        return out

    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)
        adr = self.address.raw.replace(' ', '+')
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % adr)
        resp_json_payload = response.json()
        sol = resp_json_payload['results'][0]
        dic_address = {}
        for d in sol['address_components']:
            dic_address[d['types'][0]] = d
        country = Country.objects.filter(code=dic_address['country']['short_name'])
        if len(country):
            country = country[0]
        else:
            country = Country(code=dic_address['country']['short_name'], name=dic_address['country']['long_name'])
            country.save()
        state = State.objects.filter(country=country, name=dic_address['administrative_area_level_1']['long_name'])
        if len(state):
            state = state[0]
        else:
            state = State(country=country, code=dic_address['administrative_area_level_1']['short_name'],
                          name=dic_address['administrative_area_level_1']['long_name'])
            state.save()
        locality = Locality.objects.filter(state=state, postal_code=dic_address['postal_code']['long_name'],
                                           name=dic_address['locality']['long_name'])
        if len(locality):
            locality = locality[0]
        else:
            locality = Locality(state=state, postal_code=dic_address['postal_code']['long_name'],
                                name=dic_address['locality']['long_name'])
            locality.save()
        self.address.locality = locality
        self.address.latitude = sol['geometry']['location']['lat']
        self.address.longitude = sol['geometry']['location']['lng']
        self.address.route = dic_address['route']['long_name']
        self.address.street_number = dic_address['street_number']['long_name']
        self.address.save()
        super(Doctor, self).save(*args, **kwargs)

    def as_json(self):
        return {'doctor': self.full_name(), 'lat': self.address.latitude, 'link': '/doc/%s/' % self.slug,
                'lng': self.address.longitude, 'speciality': self.get_speciality(),
                'locality': self.address.locality.name, 'img': self.picture if self.picture else None}


class DoctorForm(ModelForm):
    name = 'doctorform'

    def __init__(self, *args, **kw):
        super(DoctorForm, self).__init__(*args, **kw)
        self.fields['speciality'].widget.attrs['class'] = 'select2'
        self.fields['title'].widget.attrs['class'] = 'select2-nosearch'
        self.fields['timezone'].widget.attrs['class'] = 'select2'

    class Meta:
        model = Doctor
        fields = ['speciality', 'title', 'address', 'telephone', 'vat_number', 'timezone', 'can_recharge']


class SettingsForm(ModelForm):
    name = 'settingsform'
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    def __init__(self, *args, **kw):
        super(SettingsForm, self).__init__(*args, **kw)
        self.fields['start_time'].widget.attrs['class'] = 'clockpicker'
        self.fields['end_time'].widget.attrs['class'] = 'clockpicker'

    class Meta:
        model = Doctor
        fields = ['start_time', 'end_time', 'view_busy_slot', 'view_in_list']


class TextForm(ModelForm):
    name = 'textform'

    def __init__(self, *args, **kw):
        super(TextForm, self).__init__(*args, **kw)

    class Meta:
        model = Doctor
        fields = ['text_rdv', 'text_horaires']


class ColorForm(ModelForm):
    name = 'colorform'

    def __init__(self, *args, **kw):
        super(ColorForm, self).__init__(*args, **kw)
        self.fields['free_slot_color'].widget.attrs['class'] = 'colorpicker'
        self.fields['booked_slot_color'].widget.attrs['class'] = 'colorpicker'

    class Meta:
        model = ColorSlot
        fields = ['free_slot_color', 'booked_slot_color']
