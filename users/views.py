# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from users.models import UserProfile, UserProfileForm, ProfileForm
from utils.perms import string_random
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import views


def home(request):
    c = {}
    if request.user.is_authenticated():
        # doctors
        if request.user.is_superuser:
            # admin
            c['list'] = UserProfile.objects.all()
        else:
            c['list'] = UserProfile.objects.filter(view_in_list=True)
    else:
        c['list'] = UserProfile.objects.filter(view_in_list=True)
    return render(request, 'list.tpl', c)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    c = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error")
    else:
        messages.error(request, "Error")
        c['form'] = UserProfileForm()
        c['url'] = "/user/add_user/"
        c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def profile(request, slug):
    c = {}
    doc = UserProfile.objects.get(slug=slug)
    c['doctor'] = doc
    return render(request, 'profile.tpl', c)


def calendar_user(request, slug):
    c = {}
    userp = get_object_or_404(UserProfile, slug=slug)
    c['doctor'] = userp
    today = datetime.now().date()
    c['slots'] = []
    slots = []
    if request.user.is_authenticated():
        slots = userp.slots.all()
    elif userp.view_busy_slot is True:
        slots = userp.slots.filter(date__gte=today)
    else:
        slots = userp.slots.filter(date__gte=today, patient_id__isnull=False)
    for s in slots:
        c['slots'].append(s.as_json())
    if len(c['slots']) == 0:
        del c['slots']
    return render(request, 'calendar.tpl', c)


@login_required
def model_calendar(request, slug):
    c = {}
    userp = get_object_or_404(UserProfile, slug=slug)
    if userp.user != request.user:
        return HttpResponseRedirect('/')
    else:
        c['doctor'] = userp
        c['templateslots'] = userp.get_all_slottemplates()
        c['fullcalendar_ref_date'] = settings.FULLCALENDAR_REF_DATE
        return render(request, 'model.tpl', c)


def reminder_slot(request, slug):
    return HttpResponseRedirect('/')


def remove_slot(request, slug, slot_id):
    return HttpResponseRedirect('/')


def find_slot(request, slug, input):
    # AJAX TOUSSA
    return HttpResponseRedirect('/')


@login_required
def update_user(request):
    c = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            up = form.save()
            if 'email' in form.changed_data:
                up.confirm = string_random(32)
                up.user.is_active = False
                up.user.save()
                up.save()
            #    # SENT MAIL
                print str(up.user.email) + ' : ' + settings.WEBSITE_URL + 'confirm/' + str(up.id) + '/' + str(up.confirm) + '/'
                c['mail'] = True
            return render(request, 'valid.tpl', c)
        else:
            messages.error(request, "Error")
    else:
        c['form'] = ProfileForm(instance=request.user.userprofile)
        c['url'] = "/user/update_user/"
        c['title'] = _("Update user")
    return render(request, 'form.tpl', c)


def create_user(request):
    c = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            print "SENT MAIL"
            up = form.save()
            up.user.is_active = False
            up.confirm = string_random(32)
            up.user.save()
            up.save()
            print str(up.user.email) + ' : ' + settings.WEBSITE_URL + 'confirm/' + str(up.id) + '/' + str(up.confirm) + '/'
            c['mail'] = True
            return render(request, 'valid.tpl', c)
        else:
            messages.error(request, "Error")
    else:
        c['form'] = UserProfileForm()
        c['url'] = "/user/create_user/"
        c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def confirm_user(request, user_id, text):
    up = UserProfile.objects.get(id=user_id)
    if up.confirm == text:
        up.confirm = None
        up.user.is_active = True
        up.user.save()
        up.save()
        return render(request, 'valid.tpl', c)
