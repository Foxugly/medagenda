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
from users.models import UserProfile, UserProfileForm, PersonalDataForm, TextForm, SettingsForm, ColorForm, ColorSlot, \
    MiniInvoiceForm, NoFreeMiniInvoiceForm, TypePrice, Invoice
from utils.toolbox import string_random
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.utils import formats
from django.utils.dateformat import format


def home(request):
    c = {}
    if request.user.is_authenticated():
        # TODO mettre à jour les invoices
        # TODO foutre un dashboard avec
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
            # TODO SENT MAIL
            print str(u.user.email)
            return HttpResponseRedirect('/')
        else:
            c['form'] = form
            messages.error(request, "Error")
    else:
        c['form'] = UserProfileForm()
    c['url'] = "/user/add_user/"
    c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def profile(request, slug=None):
    doc = get_object_or_404(UserProfile, slug=slug) if slug else request.user.userprofile
    c = {'doctor': doc}
    return render(request, 'profile.tpl', c)


def calendar_user(request, slug=None):
    userp = get_object_or_404(UserProfile, slug=slug) if slug else request.user.userprofile
    c = {'doctor': userp}
    today = datetime.now().date()
    c['slots'] = []
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
def model_calendar(request):
    c = {'doctor': request.user.userprofile, 'slot_type': settings.SLOT_TYPE,
         'slottemplates': request.user.userprofile.get_all_slottemplates(),
         'fullcalendar_ref_date': settings.FULLCALENDAR_REF_DATE}
    return render(request, 'model.tpl', c)


def reminder_slot(request, slug):
    print slug
    # TODO ajouter la fonction de rappel de slots
    return HttpResponseRedirect('/')


def remove_slot(request, slug, slot_id):
    print slug
    print slot_id
    # TODO déterminer la façon d'annuler un rendez-vous (manuel/automatique)
    return HttpResponseRedirect('/')


def search_doctor(request):
    # TODO fonction de recherche (jouer avec Q)
    return HttpResponseRedirect('/')


    # TODO gérer les abonnements, le renouvellement,....


@login_required
def user_settings(request):
    up = request.user.userprofile
    c = {'userprofile_id': request.user.userprofile.id,
         'personal_data_form': PersonalDataForm(instance=up),
         'settings_form': SettingsForm(instance=up), 'avatar': up.picture,
         'text_form': TextForm(instance=up), 'color_forms': [],
         'password_change_form': PasswordChangeForm(user=request.user),
         'invoice': up.get_active_invoice(),
         'new_invoice': MiniInvoiceForm() if not up.already_use_free_invoice() else NoFreeMiniInvoiceForm()}
    for st in settings.SLOT_TYPE:
        d = {'id': up.get_colorslot(st[0]).id, 'name': st[1],
             'form': ColorForm(instance=up.get_colorslot(st[0]))}
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
            # TODO SENT MAIL
            print str(up.user.email) + ' : ' + settings.WEBSITE_URL + 'confirm/' + str(up.id) + '/' + str(
                up.confirm) + '/'
            c['mail'] = True
            return render(request, 'valid.tpl', c)
        else:
            messages.error(request, "Error")
            c['form'] = form
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
def password(request):
    results = {}
    if request.is_ajax():
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
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


@login_required
def invoice_add(request):
    results = {}
    if request.is_ajax():
        up = request.user.userprofile
        tp = TypePrice.objects.get(id=request.POST['type_price'][0])
        if tp:
            if len(up.invoices.all()):
                i = up.invoices.order_by('-date_end')[0]
                if i.date_end > datetime.date(datetime.today()):
                    f_day = i.date_end + relativedelta(days=+1)
                    active = False
                else:
                    f_day = datetime.today()
                    active = True
            else:
                f_day = datetime.today()
                active = True
            new_invoice = Invoice(type_price=tp, date_start=f_day,
                                  date_end=f_day + relativedelta(months=+tp.num_months), price_exVAT=int(tp.price_exVAT),
                                  active=active)
            new_invoice.save()
            up.invoices.add(new_invoice)
            results['return'] = True
            results['id'] = new_invoice.id
            results['type_price'] = str(new_invoice.type_price)
            date_format = formats.get_format('DATE_FORMAT')
            results['date_start'] = format(new_invoice.date_start, date_format)
            results['date_end'] = format(new_invoice.date_end, date_format)
        else:
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


@login_required
def invoice_remove(request, invoice_id):
    results = {}
    if request.is_ajax():
        up = request.user.userprofile
        i = Invoice.objects.get(id=invoice_id)
        if i in up.invoices.all():
            up.invoices.remove(i)
            i.delete()
            results['return'] = True
        else:
            results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))
