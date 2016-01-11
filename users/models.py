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
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django import forms
from django.forms import ModelForm


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), null=True)
    current_doctor = models.ForeignKey('doctor.Doctor', verbose_name=_(u'Current doctor'), related_name='current_doctor', null=True)
    doctors = models.ManyToManyField('doctor.Doctor', verbose_name=_(u'Doctors'), related_name='doctors', blank=True)
    language = models.CharField(verbose_name=_(u'language'), max_length=8, choices=settings.LANGUAGES, default=1)
    confirm = models.TextField(verbose_name=_(u'Confirm key'), blank=True, null=True)
    accept = models.BooleanField(verbose_name=_(
            u'I accept the terms and conditions of use of Medagenda (see <a href="/conditions/"> here </a>)'),
            blank=False, null=False, default=False)

    def __str__(self):
        return u"userprofile : %s" % self.user.username

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u, language=settings.LANGUAGES[0])[0])


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserProfileForm(ModelForm):
    error_messages = {
        'not_accepted': _("You must accept the terms and conditions of use of Medagenda"),
    }

    class Meta:
        model = UserProfile
        fields = ['language', 'accept']

    def __init__(self, *args, **kw):
        super(UserProfileForm, self).__init__(*args, **kw)
        self.fields['language'].widget.attrs['class'] = 'select2-nosearch'

    def clean_accept(self):
        accept = self.cleaned_data.get('accept')
        if not accept:
            self.add_error('accept', forms.ValidationError(self.error_messages['not_accepted'], code='not_accepted'))
        return accept
