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
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from address.models import AddressField
from django.forms import ModelForm
from django.utils.text import slugify
from agenda.models import WeekTemplate, DayTemplate, Slot
from timezone_field import TimeZoneField


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
        ret = u'(%d %s) : %d euros ' % (self.num_months, _(u'month') if self.num_months < 2 else _(u'months'), self.price_exVAT)
        ret += u'%s' % _(u'excl. VAT')
        return ret


class Invoice(models.Model):
    type_price = models.ForeignKey(TypePrice, verbose_name=_(u'Type of account'), blank=False)
    date_creation = models.DateField(verbose_name=_(u'Creation_date'), auto_now_add=True)
    date_start = models.DateField(verbose_name=_(u'Start date'), blank=False)
    date_end = models.DateField(verbose_name=_(u'End date'), blank=False)
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    price_exVAT = models.FloatField(verbose_name=_('Price excl. VAT'), blank=False, default=0.0)
    VAT = models.FloatField(verbose_name=_('VAT (%)'), blank=False, default=21)
    price_VAT = models.FloatField(verbose_name=_('Price VAT'), blank=True, default=0.0)
    price_incVAT = models.FloatField(verbose_name=_('Price inc. VAT'), blank=True, default=0.0)
    paid = models.BooleanField(verbose_name=_('Paid'), default=False)
    date_paid = models.DateField(verbose_name=_('date Paid'), blank=True, null=True)
    note_paid = models.CharField(verbose_name=_(u'note paid'), max_length=100, blank=True)
    show = models.BooleanField(verbose_name=_('Show'), default=True)

    def save(self, *args, **kwargs):
        super(Invoice, self).save(*args, **kwargs)
        if self.price_incVAT != ((self.VAT/100) * self.price_exVAT) + self.price_exVAT:
            self.price_VAT = (self.VAT/100) * self.price_exVAT
            self.price_incVAT = self.price_VAT + self.price_exVAT
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


class UserProfile(models.Model):
    MEDECINE_CHOICES = settings.MEDECINE_CHOICES
    TITLE_CHOICES = settings.TITLE_CHOICES

    title = models.IntegerField(verbose_name=_(u'Title'), choices=TITLE_CHOICES)
    user = models.OneToOneField(User, verbose_name=_('User'))
    picture = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH, blank=True, null=True)
    speciality = models.IntegerField(verbose_name=_(u'Speciality'), choices=MEDECINE_CHOICES)
    slug = models.SlugField(verbose_name=_(u'slug'), max_length=50, blank=True)
    language = models.CharField(verbose_name=_(u'language'), max_length=8, choices=settings.LANGUAGES, default=1)
    vat_number = models.CharField(verbose_name=_(u'VAT number'), max_length=20, blank=True)
    telephone = models.CharField(verbose_name=_(u'Telephone'), max_length=20, blank=True)
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

    def __str__(self):
        return u"userprofile : %s" % self.user.username

    def get_title(self):
        return u"%s" % self.TITLE_CHOICES[self.title - 1][1]

    def full_name(self):
        return u"%s %s" % (self.get_title(), self.real_name())

    def real_name(self):
        return u"%s %s" % (self.user.first_name, self.user.last_name)

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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.real_name())
        super(UserProfile, self).save(*args, **kwargs)

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

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u, language=settings.LANGUAGES[0])[0])


class UserProfileForm(ModelForm):
    username = forms.CharField(label=_(u"Username"), max_length=50)
    first_name = forms.CharField(label=_(u'First name'), max_length=50)
    last_name = forms.CharField(label=_(u'Last name'), max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def __init__(self, *args, **kw):
        super(UserProfileForm, self).__init__(*args, **kw)
        self.fields['speciality'].widget.attrs['class'] = 'select2'
        self.fields['title'].widget.attrs['class'] = 'select2-nosearch'
        self.fields['language'].widget.attrs['class'] = 'select2-nosearch'
        self.fields['timezone'].widget.attrs['class'] = 'select2'

    def save(self, *args, **kw):
        up = super(UserProfileForm, self).save(commit=False)
        new_user = User.objects.create_user(self.cleaned_data.get('username'), email=self.cleaned_data.get('email'),
                                            password=self.cleaned_data.get('password'))
        new_user.last_name = self.cleaned_data.get('last_name')
        new_user.first_name = self.cleaned_data.get('first_name')
        new_user.email = self.cleaned_data.get('email')
        new_user.save()
        up.user = new_user
        up.save()
        return up

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'repeat_password', 'speciality', 'title', 'first_name', 'last_name',
                  'address', 'email', 'telephone', 'vat_number', 'language', 'timezone']


class PersonalDataForm(ModelForm):
    first_name = forms.CharField(label=_(u'Prénom'), max_length=50)
    last_name = forms.CharField(label=_(u'Nom'), max_length=50)
    email = forms.EmailField()

    def __init__(self, *args, **kw):
        super(PersonalDataForm, self).__init__(*args, **kw)
        self.fields['first_name'].initial = kw['instance'].user.first_name
        self.fields['last_name'].initial = kw['instance'].user.last_name
        self.fields['email'].initial = kw['instance'].user.email
        self.fields['speciality'].widget.attrs['class'] = 'select2'
        self.fields['title'].widget.attrs['class'] = 'select2-nosearch'
        self.fields['language'].widget.attrs['class'] = 'select2-nosearch'
        self.fields['timezone'].widget.attrs['class'] = 'select2'

    def save(self, *args, **kw):
        up = super(PersonalDataForm, self).save(commit=False)
        up.user.last_name = self.cleaned_data.get('last_name')
        up.user.first_name = self.cleaned_data.get('first_name')
        up.user.email = self.cleaned_data.get('email')
        up.user.save()
        up.save()
        return up

    class Meta:
        model = UserProfile
        fields = ['speciality', 'title', 'first_name', 'last_name', 'address', 'email', 'telephone', 'vat_number',
                  'language', 'timezone']


class SettingsForm(ModelForm):
    def __init__(self, *args, **kw):
        super(SettingsForm, self).__init__(*args, **kw)
        self.fields['start_time'].widget.attrs['class'] = 'clockpicker'
        self.fields['end_time'].widget.attrs['class'] = 'clockpicker'

    class Meta:
        model = UserProfile
        fields = ['start_time', 'end_time', 'view_busy_slot', 'view_in_list']


class TextForm(ModelForm):
    def __init__(self, *args, **kw):
        super(TextForm, self).__init__(*args, **kw)

    class Meta:
        model = UserProfile
        fields = ['text_rdv', 'text_horaires']


class ColorForm(ModelForm):
    def __init__(self, *args, **kw):
        super(ColorForm, self).__init__(*args, **kw)
        self.fields['free_slot_color'].widget.attrs['class'] = 'colorpicker'
        self.fields['booked_slot_color'].widget.attrs['class'] = 'colorpicker'

    class Meta:
        model = ColorSlot
        fields = ['free_slot_color', 'booked_slot_color']
