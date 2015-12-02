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
# Create your models here.


class Patient(models.Model):
    mail = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
