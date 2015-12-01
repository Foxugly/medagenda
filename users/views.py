# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from users.models import UserProfile, UserProfileForm
from utils.perms import get_context
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from datetime import datetime, timedelta, time

def home(request):
    if request.user.is_authenticated():
        # doctors
        if request.user.is_superuser:
            # admin
            userprofiles = UserProfile.objects.filter(view_in_list=True)
            c = get_context(request)
            c['list'] = userprofiles
            return render_to_response('list.tpl', c)
    else :
        userprofiles = UserProfile.objects.filter(view_in_list=True)
        c = get_context(request)
        c['list'] = userprofiles
        return render_to_response('list.tpl', c)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    c = get_context(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print('VALID')
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error")
            print('ERROR1')
    else:
        messages.error(request, "Error")
        print('ERROR2')
        c['form'] = UserProfileForm()
        c['url'] = "/user/adduser/"
        c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)

def profile_user(request,slug):
    c = get_context(request)
    user = get_object_or_404(UserProfile,slug=slug)
    c['doctor'] = user
    return render(request, 'profile.tpl', c)

def calendar_user(request,slug):
    c = get_context(request)
    user = get_object_or_404(UserProfile,slug=slug)
    c['doctor'] = user
    today = datetime.now().date()
    c['slots'] = []
    slots = user.slots.filter(date__gte=today)
    for s in slots:
        c['slots'].append(s.as_json())
    print c['slots']
    return render(request, 'calendar.tpl', c)

@login_required
def model_calendar(request, slug):
    c = get_context(request)
    user = get_object_or_404(UserProfile,slug=slug)
    c['doctor'] = user
    return render(request, 'model.tpl', c)

def reminder_slot(request, slug):
     return HttpResponseRedirect('/')

def remove_slot(request,slug,slot_id):
    return HttpResponseRedirect('/')

def find_slot(request,slug,input):
    # AJAX TOUSSA
    return HttpResponseRedirect('/')
