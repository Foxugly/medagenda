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
from users.models import UserProfile, UserProfileForm, ProfileForm
from utils.perms import get_context, string_random
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth import views
from django.views.decorators.debug import sensitive_post_parameters

def home(request):
    c = get_context(request)
    if request.user.is_authenticated():
        # doctors
        if request.user.is_superuser:
            # admin
            c['list'] = UserProfile.objects.all()
        else:
            c['list'] = UserProfile.objects.filter(view_in_list=True)
    else:
        c['list'] = UserProfile.objects.filter(view_in_list=True)
    return render_to_response('list.tpl', c)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    c = get_context(request)
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
        c['enctype_form'] = 'enctype="multipart/form-data"'
        c['url'] = "/user/add_user/"
        c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def profile(request, slug):
    c = get_context(request)
    doc = UserProfile.objects.get(slug=slug)
    c['doctor'] = doc
    return render(request, 'profile.tpl', c)


def calendar_user(request, slug):
    c = get_context(request)
    user = get_object_or_404(UserProfile, slug=slug)
    c['doctor'] = user
    today = datetime.now().date()
    c['slots'] = []
    slots = []
    if request.user.is_authenticated():
        slots = user.slots.all()
    elif user.view_busy_slot == True:
        slots = user.slots.filter(date__gte=today)
    else:
        slots = user.slots.filter(date__gte=today, patient_id__isnull=False)
    for s in slots:
        c['slots'].append(s.as_json())
    if len(c['slots']) == 0:
        del c['slots']
    return render(request, 'calendar.tpl', c)


@login_required
def model_calendar(request, slug):
    c = get_context(request)
    user = get_object_or_404(UserProfile, slug=slug)
    if user.user != request.user :
        return HttpResponseRedirect('/')
    else :
        c['doctor'] = user
        c['templateslots'] = user.get_all_slottemplates()
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
    c = get_context(request)
    user = c['userprofile']
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            u = form.save()
            if 'email' in form.changed_data:
                u.confirm = string_random(32)
                u.user.is_active = False
                u.user.save()
                u.save()

            #    print "ICICICICICICICI"
            #    # SENT MAIL
                print str(u.user.email) + ' : ' + settings.WEBSITE_URL + 'confirm/' + str(u.id) + '/' + str(u.confirm) + '/'
            return HttpResponseRedirect('/user/update_user/')
        else:
            messages.error(request, "Error")
    else:
        c['form'] = ProfileForm(instance=user)
        #c['enctype_form'] = 'enctype="multipart/form-data"'
        c['url'] = "/user/update_user/"
        c['title'] = _("Update user")
    return render(request, 'form.tpl', c)

def create_user(request):
    c = get_context(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            print "SENT MAIL"
            u = form.save()
            u.user.is_active = False
            u.confirm = string_random(32)
            u.user.save()
            u.save()
            print str(u.user.email) + ' : ' + settings.WEBSITE_URL + 'confirm/' + str(u.id) + '/' + str(u.confirm) + '/'
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error")
    else:
        c['form'] = UserProfileForm()
        c['enctype_form'] = 'enctype="multipart/form-data"'
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


def password_change(request):
    return views.password_change(request, template_name='form.tpl', extra_context=get_context(request)) 

def password_change_done(request):
    return views.password_change_done(request, template_name='valid.tpl', extra_context=get_context(request)) 