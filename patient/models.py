# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    email = models.EmailField(verbose_name=_(u'Email'), blank=True, null=True)
    first_name = models.CharField(verbose_name=_(u'First name'), max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name=_(u'Last_name'), max_length=100, blank=True, null=True)
    telephone = models.CharField(verbose_name=_(u'Telephone'), max_length=20, blank=True, null=True)
    active = models.BooleanField(verbose_name=_(u'Confirmed'), default=False)
    confirm = models.TextField(verbose_name=_(u'Confirm key'), blank=True, null=True)


    def __str__(self):
        return str(self.email)

    def as_json(self):
        return dict(id=self.id, email=self.email, first_name=self.first_name, last_name=self.last_name,
                    telephone=self.telephone)


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['email', 'first_name', 'last_name', 'telephone']
