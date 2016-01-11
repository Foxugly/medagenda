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
from users.models import UserProfile, UserCreateForm, UserProfileForm
from doctor.models import DoctorForm, TextForm, SettingsForm, ColorForm, ColorSlot, \
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
from datetime import datetime, date
from django.utils import formats
from django.utils.dateformat import format
from django.db.models import Q
from utils.mail import mail_user_welcome
from utils.invoice import PrintInvoice
from doctor.models import Doctor


def home(request):
    c = {}
    if request.user.is_authenticated():
        if request.user.is_superuser:  # admin
            c['list'] = Doctor.objects.all()
            return render(request, 'list.tpl', c)
        else:
            # TODO MUST BE RUN BY A CRON DAEMON
            old_i = request.user.userprofile.invoices.objects.get(active=True)
            i = request.user.userprofile.invoices.objects.filter(date_start__lte=date.today(),
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
        if ucform.is_valid() and upform.is_valid() and docform.is_valid():
            u = ucform.save()
            up = upform.save()
            doc = docform.save()
            doc.refer_userprofile = up
            for st in settings.SLOT_TYPE:
                doc.get_colorslot(st[0])
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
            c['form'] = [ucform, upform, docform]
            messages.error(request, "Error")
    else:
        c['form'] = [UserCreateForm(), UserProfileForm(), DoctorForm()]
    c['url'] = "/user/add_user/"
    c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)


def profile(request, slug=None):
    doc = get_object_or_404(Doctor, slug=slug) if slug else request.user.userprofile.current_doctor
    c = {'doctor': doc}
    return render(request, 'profile.tpl', c)


def calendar_user(request, slug=None):
    doc = get_object_or_404(Doctor, slug=slug) if slug else request.user.userprofile.current_doctor
    c = {'doctor': doc}
    today = datetime.now().date()
    c['slots'] = []
    if request.user.is_authenticated():
        slots = doc.slots.all()
    elif doc.view_busy_slot is True:
        slots = doc.slots.filter(date__gte=today)
    else:
        slots = doc.slots.filter(date__gte=today, patient_id__isnull=False)
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
    print "reminder_slot"
    print slug
    # TODO ajouter la fonction de rappel de slots
    return HttpResponseRedirect('/')


def remove_slot(request, slug, slot_id):
    print "remove_slot"
    print slug
    print slot_id
    # TODO déterminer la façon d'annuler un rendez-vous (manuel/automatique)
    return HttpResponseRedirect('/')


def search_doctor(request):
    # TODO finaliser
    results = {}
    if request.is_ajax():
        s = 'text'
        if request.user.is_superuser:
            results['list'] = UserProfile.objects.filter(Q(address__contains=s) |
                                                         Q(user__firstname__contains=s) | Q(user__lastname__contains=s))
        else:
            results['list'] = UserProfile.objects.filter(
                    Q(address__contains=s) | Q(user__firstname__contains=s) | Q(user__lastname__contains=s),
                    Q(view_in_list=True))
        results['return'] = True
    else:
        results['return'] = False

    return HttpResponse(json.dumps(results))

    # TODO gérer les abonnements, le renouvellement,....


@login_required
def user_settings(request):
    up = request.user.userprofile
    c = {'userprofile_id': request.user.userprofile.id,
         'personal_data_form': DoctorForm(instance=up.current_doctor),
         'settings_form': SettingsForm(instance=up.current_doctor), 'avatar': up.picture,
         'text_form': TextForm(instance=up.current_doctor), 'color_forms': [],
         'password_change_form': PasswordChangeForm(user=request.user),
         'invoice': up.get_active_invoice(),
         'new_invoice': MiniInvoiceForm() if not up.already_use_free_invoice() else NoFreeMiniInvoiceForm()}
    for st in settings.SLOT_TYPE:
        d = {'id': up.get_colorslot(st[0]).id, 'name': st[1],
             'form': ColorForm(instance=up.current_doctor.get_colorslot(st[0]))}
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
            mail_user_welcome(request, up, True)
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
    up = get_object_or_404(UserProfile, user__id=user_id)
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
        form = DoctorForm(request.POST, instance=request.user.userprofile.current_doctor)
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
def text_profil(request):
    results = {}
    if request.is_ajax():
        form = TextForm(request.POST, instance=request.user.userprofile.current_doctor)
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
        # inst = ColorSlot.objects.get(id=color_id)
        inst = get_object_or_404(ColorSlot, id=color_id)
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
        tp = TypePrice.objects.filter(id=request.POST['type_price'][0])[0]
        up.can_recharge = request.POST['can_recharge']
        up.save()
        # TODO a vérifier
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
                                  date_end=f_day + relativedelta(months=+tp.num_months),
                                  price_exVAT=int(tp.price_exVAT), active=active)
            new_invoice.save()
            up.invoices.add(new_invoice)
            results['return'] = True
            results['id'] = new_invoice.id
            results['type_price'] = str(new_invoice.type_price)
            date_format = formats.get_format('DATE_INPUT_FORMATS')[0]
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


@login_required
def invoices(request):
    data = []
    titles = ['ID', _(u'Creation date'), _(u'Type of subscription'), _(u'Start date'), _('End date'),
              _(u'Price inc. VAT'), _(u'date paid')]
    date_format = formats.get_format('DATE_INPUT_FORMATS')[0]
    print 'invoices'
    for i in request.user.userprofile.invoices.all().order_by('id'):
        if i.paid:
            paid = format(i.date_paid, date_format)
        else:
            paid = '<a href="link/sofort" class="btn btn-danger" role="button">%s</a>' % _("Pay now")
        data.append([i.id, format(i.date_creation, date_format), i.type_price, format(i.date_start, date_format),
                     format(i.date_end, date_format), "%.2f euros" % i.price_incVAT, paid])
    c = {'title': 'Invoices', 'table': {'data': data, 'titles': titles}}
    return render(request, 'table.tpl', c)
