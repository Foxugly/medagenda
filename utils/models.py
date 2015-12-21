# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.forms import ModelForm


class Faq(models.Model):
    lang = models.CharField(verbose_name=_(u'language'), max_length=8, choices=settings.LANGUAGES, default=1)
    question = models.TextField(verbose_name=_(u'Question'), blank=True, null=True)
    answer = models.TextField(verbose_name=_(u'Answer'), blank=True, null=True)


class FaqForm(ModelForm):

    def __init__(self, *args, **kw):
        super(FaqForm, self).__init__(*args, **kw)

    class Meta:
        model = Faq
        fields = ['lang', 'question', 'answer', ]


class ContactForm(forms.Form):
    sender = forms.EmailField(label=_(u'Your email address'))
    subject = forms.CharField(label=_(u'Subject'))
    message = forms.CharField(label=_(u'Message'),widget=forms.Textarea)
    cc_myself = forms.BooleanField(label=_(u'sent me the mail'))
