# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from users.models import UserProfile, UserCreateForm, UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from doctor.models import DoctorForm, Invoice, MiniInvoiceForm
from utils.toolbox import string_random
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.conf import settings
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from utils.mail import mail_user_welcome
from utils.invoice import PrintInvoice
from doctor.models import Doctor
import json
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home(request):
    c = {}
    if request.user.is_authenticated():
        if request.user.is_superuser:  # admin
            c['list'] = Doctor.objects.all()
            return render(request, 'list.tpl', c)
        else:
            # TODO MUST BE RUN BY A CRON DAEMON
            old_i = request.user.userprofile.current_doctor.invoices.objects.get(active=True)
            i = request.user.userprofile.current_doctor.invoices.objects.filter(date_start__lte=date.today(),
                                                                                date_end__gte=date.today())
            if len(i):
                current_i = i[0]
                if old_i is not current_i:
                    old_i.active = False
                    old_i.save()
                    current_i.active = True
                    current_i.save()
                    new_pi = PrintInvoice(i[0], request.user.userprofile)
                    new_pi.save()
                    # TODO send mail avec invoice
            else:
                if request.user.userprofile.can_recharge:
                    old_i.active = False
                    old_i.save()
                    f_day = datetime.today()
                    new_i = Invoice(type_price=old_i.type_price, date_start=f_day,
                                    date_end=f_day + relativedelta(months=+old_i.type_price.num_months),
                                    price_exVAT=int(old_i.type_price.price_exVAT), active=True)
                    new_i.save()
                    new_pi = PrintInvoice(new_i, request.user.userprofile)

                    new_pi.save()
                    # TODO send mail avec invoice
                else:
                    # TODO send mail pour dire va mettre à jour sinon dans 7 jours, on cloture
                    # gérer la cloture
                    print "HERE"
            # ----------------------
            # TODO préparer les data pour le dashboard
            return render(request, 'dashboard.tpl', c)
    else:
        c['list'] = Doctor.objects.filter(view_in_list=True)
        return render(request, 'list.tpl', c)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    c = {}
    if request.method == 'POST':
        ucform = UserCreateForm(request.POST)
        upform = UserProfileForm(request.POST)
        docform = DoctorForm(request.POST)
        invoiceform = MiniInvoiceForm(request.POST)
        if ucform.is_valid() and upform.is_valid() and docform.is_valid():
            i = invoiceform.save()
            u = ucform.save()
            up = upform.save()
            doc = docform.save()
            doc.refer_userprofile = up
            for st in settings.SLOT_TYPE:
                doc.get_colorslot(st[0])
            doc.invoices.add(i)
            doc.save()
            up.user = u
            up.doctors.add(doc)
            up.current_doctor = doc
            up.save()
            doc.set_slug()
            doc.save()
            mail_user_welcome(request, up, False)
            return HttpResponseRedirect('/')
        else:
            c['form'] = [ucform, upform, docform, invoiceform]
            messages.error(request, "Error")
    else:
        c['form'] = [UserCreateForm(), UserProfileForm(), DoctorForm(), MiniInvoiceForm()]
    c['url'] = "/user/add_user/"
    c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def create_user(request):
    c = {}
    if request.method == 'POST':
        ucform = UserCreateForm(request.POST)
        upform = UserProfileForm(request.POST)
        docform = DoctorForm(request.POST)
        invoiceform = MiniInvoiceForm(request.POST)
        if ucform.is_valid() and upform.is_valid() and docform.is_valid():
            i = invoiceform.save()
            u = ucform.save()
            up = upform.save()
            u.is_active = False
            u.save()
            up.confirm = string_random(32)
            doc = docform.save()
            doc.refer_userprofile = up
            for st in settings.SLOT_TYPE:
                doc.get_colorslot(st[0])
            doc.invoices.add(i)
            doc.save()
            up.user = u
            up.doctors.add(doc)
            up.current_doctor = doc
            up.save()
            doc.set_slug()
            doc.save()
            mail_user_welcome(request, up, True)
            c['mail'] = True
            return render(request, 'valid.tpl', c)
        else:
            c['form'] = [ucform, upform, docform, invoiceform]
            messages.error(request, "Error")
    else:
        c['form'] = [UserCreateForm(), UserProfileForm(), DoctorForm(), MiniInvoiceForm()]
    c['url'] = "/user/create_user/"
    c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def confirm_user(request, user_id, text):
    up = get_object_or_404(UserProfile, user__id=user_id)
    if up.confirm == text:
        up.confirm = None
        up.user.is_active = True
        up.user.save()
        up.save()
        return render(request, 'valid.tpl')


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
