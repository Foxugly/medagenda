# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import render
from django.http import HttpResponse
from django.utils import translation
from django import http
import json
from django.conf import settings
from utils.models import Faq, ContactForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


def lang(request):
    results = {}
    if request.is_ajax():
        user_language = request.POST['lang']
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        results['return'] = True
        response = http.HttpResponse(json.dumps(results))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        return response
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


def faq(request):
    c = {}
    f = Faq.objects.filter(lang=request.LANGUAGE_CODE)
    if len(f):
        c ['faq'] = f
    return render(request, 'faq.tpl', c)


def contact(request):
    c = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print "SENT MAIL contact"
            c['mail'] = True
            return render(request, 'valid.tpl', c)
        else:
            messages.error(request, "Error")
    else:
        c['form'] = ContactForm()
        c['url'] = "/contact/"
        c['title'] = _("Contact us")
    return render(request, 'form.tpl', c)


def about(request):
    return render(request, 'about.tpl')


def offer(request):
    return render(request, 'offer.tpl')

def conditions(request):
    return render(request, 'conditions.tpl')