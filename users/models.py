# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from string import printable
from django.db import models
from django.db.models import signals, Q
from django.contrib.auth import models as authmod
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from colorfield.fields import ColorField
from address.models import AddressField
from django.forms import ModelForm
from django.utils.text import slugify
from agenda.models import WeekTemplate, DayTemplate, Slot


class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()


class UserProfile(models.Model):
    MEDECINE_CHOICES = settings.MEDECINE_CHOICES
    TITLE_CHOICES = settings.TITLE_CHOICES

    title = models.IntegerField(verbose_name=_(u'Title'), choices=TITLE_CHOICES, default=2)
    user = models.OneToOneField(User, verbose_name=_('User'))
    picture = models.ImageField(upload_to='pic', blank=True, null=True)
    speciality = models.IntegerField(verbose_name=_(u'Speciality'), choices=MEDECINE_CHOICES)
    slug = models.SlugField(verbose_name=_(u'slug'), max_length=50, blank=True)
    language = models.CharField(verbose_name=_(u'language'), max_length=2, choices=settings.LANGUAGES)
    vat_number = models.CharField(verbose_name=_(u'VAT number'), max_length=20, blank=True)
    telephone = models.CharField(verbose_name=_(u'Telephone'), max_length=20, blank=True)
    address = AddressField()
    start_time = models.TimeField(verbose_name=_(u'Start time'), blank=False, default="09:00")
    end_time = models.TimeField(verbose_name=_(u'End time'), blank=False, default="18:00")
    free_price_free_slot_color = ColorField(default='#73B5EB')
    free_price_booked_slot_color = ColorField(default='#F64636')
    nhs_price_free_slot_color = ColorField(default='#73EB79')  # nhs = national health service price
    nhs_price_booked_slot_color = ColorField(default='#F64636')
    view_busy_slot = models.BooleanField(verbose_name=_(u'Can see busy slots'))
    view_in_list = models.BooleanField(verbose_name=_(u'Can see in doctors list'))
    weektemplate = models.ForeignKey(WeekTemplate, verbose_name=_(u'Week template'), blank=True, null=True)
    slots = models.ManyToManyField(Slot, verbose_name=_(u'Slots'), blank=True)
    confirm = models.TextField(verbose_name=_(u'Confirm key'), blank=True, null=True)

    def __str__(self):
        return "userprofile : " + str(self.user.username)

    def real_name(self):
        return str(self.user.first_name + " " + self.user.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.real_name())
        super(UserProfile, self).save(*args, **kwargs)

    def get_all_slottemplates(self):
        out = []
        for dt in self.weektemplate.days.all():
            for s in dt.slots.all():
                out.append(s.as_json(dt.day, self))
        return out

    def remove_all_slottemplates(self):
        self.weektemplate.remove_all_slottemplates()

    def get_daytemplate(self, i):
        d = None
        for day in self.weektemplate.days.all():
            if day.day == i:
                d = day
        if not d:
            d = DayTemplate(day=i)
            d.save()
            self.weektemplate.add_daytemplate(d)
        return d

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u, language=settings.LANGUAGES[0])[0])


class BaseProfileForm(ModelForm):
    first_name = forms.CharField(label=_(u'Prénom'), max_length=50)
    last_name = forms.CharField(label=_(u'Nom'), max_length=50)
    email = forms.EmailField()

    def __init__(self, *args, **kw):
        super(BaseProfileForm, self).__init__(*args, **kw)
        self.fields['start_time'].widget.attrs['class'] = 'clockpicker'
        self.fields['end_time'].widget.attrs['class'] = 'clockpicker'


class ProfileForm(BaseProfileForm):

    def __init__(self, *args, **kw):
        super(ProfileForm, self).__init__(*args, **kw)
        self.fields['first_name'].initial = kw['instance'].user.first_name
        self.fields['last_name'].initial = kw['instance'].user.last_name
        self.fields['email'].initial = kw['instance'].user.email

    def save(self, *args, **kw):
        up = super(ProfileForm, self).save(commit=False)
        up.user.last_name = self.cleaned_data.get('last_name')
        up.user.first_name = self.cleaned_data.get('first_name')
        up.user.email = self.cleaned_data.get('email')
        up.user.save()
        up.save()
        return up

    class Meta:
        model = UserProfile
        exclude = ('user', 'slug', 'weektemplate', 'slots', 'confirm', 'picture')
        fields = ['picture', 'speciality', 'first_name', 'last_name', 'address', 'email', 'telephone', 'vat_number', 'language', 'start_time', 'end_time', 'free_price_free_slot_color', 'free_price_booked_slot_color', 'nhs_price_free_slot_color', 'nhs_price_booked_slot_color', 'view_busy_slot', 'view_in_list']


class UserProfileForm(BaseProfileForm):
    username = forms.CharField(label=_(u"Nom d'utilisateur"), max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def __init__(self, *args, **kw):
        super(UserProfileForm, self).__init__(*args, **kw)

    def save(self, *args, **kw):
        up = super(UserProfileForm, self).save(commit=False)
        new_user = User.objects.create_user(self.cleaned_data.get('username'), email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        new_user.last_name = self.cleaned_data.get('last_name')
        new_user.first_name = self.cleaned_data.get('first_name')
        new_user.email = self.cleaned_data.get('email')
        new_user.save()
        up.user = new_user
        up.save()
        return up

    class Meta:
        model = UserProfile
        exclude = ('user', 'slug', 'weektemplate', 'slots', 'confirm', 'picture')
        fields = ['username', 'password', 'repeat_password', 'picture', 'speciality', 'first_name', 'last_name', 'address', 'email', 'telephone', 'vat_number', 'language', 'start_time', 'end_time', 'free_price_free_slot_color', 'free_price_booked_slot_color', 'nhs_price_free_slot_color', 'nhs_price_booked_slot_color', 'view_busy_slot', 'view_in_list']
