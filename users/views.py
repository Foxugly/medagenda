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
from users.models import UserProfile, UserProfileForm, PersonalDataForm, TextForm, SettingsForm, ColorForm, ColorSlot
from utils.perms import string_random
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from datetime import datetime
from django.conf import settings


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
        form = UserProfileForm(request.POST)
        if form.is_valid():
            u = form.save()
            for st in settings.SLOT_TYPE:
                u.get_colorslot(st[0])
            u.save()
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
    # slots = []
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
        c['slot_type'] = settings.SLOT_TYPE
        c['slottemplates'] = userp.get_all_slottemplates()
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
    c = {'userprofile_id': request.user.userprofile.id,
         'personal_data_form': PersonalDataForm(instance=request.user.userprofile),
         'settings_form': SettingsForm(instance=request.user.userprofile), 'avatar': request.user.userprofile.picture,
         'text_form': TextForm(instance=request.user.userprofile), 'color_forms': []}
    for st in settings.SLOT_TYPE:
        d = {'id': request.user.userprofile.get_colorslot(st[0]).id, 'name': st[1],
             'form': ColorForm(instance=request.user.userprofile.get_colorslot(st[0]))}
        c['color_forms'].append(d)
    return render(request, 'config.tpl', c)


def create_user(request):
    c = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            up = form.save()
            up.user.is_active = False
            up.confirm = string_random(32)
            up.user.save()
            up.save()
            print "SENT MAIL"
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


def confirm_user(request, user_id, txt):
    up = UserProfile.objects.get(id=user_id)
    if up.confirm == txt:
        up.confirm = None
        up.user.is_active = True
        up.user.save()
        up.save()
        return render(request, 'valid.tpl')


@login_required
def personal_data(request):
    results = {}
    if request.is_ajax():
        form = PersonalDataForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            results['return'] = True
        else:
            results['errors'] = form.errors
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def text(request):
    results = {}
    if request.is_ajax():
        form = TextForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            results['return'] = True
        else:
            results['errors'] = form.errors
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def config(request):
    results = {}
    if request.is_ajax():
        form = SettingsForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            results['return'] = True
        else:
            results['errors'] = form.errors
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def avatar(request):
    results = {}
    if request.is_ajax():
        up = request.user.userprofile
        up.picture.delete()
        if len(request.FILES):
            up.picture = request.FILES['id_picture']
        up.save()
        results['return'] = True
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def color(request, color_id):
    results = {}
    if request.is_ajax():
        inst = ColorSlot.objects.get(id=color_id)
        form = ColorForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            results['return'] = True
        else:
            results['errors'] = form.errors
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def remove_picture(request):
    request.user.userprofile.picture = None
    request.user.profile.save()
    results = {'return': True}
    return HttpResponse(json.dumps(results))