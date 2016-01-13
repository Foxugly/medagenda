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
from users.models import UserProfile
from doctor.models import DoctorForm, TextForm, SettingsForm, ColorForm, ColorSlot, \
    MiniInvoiceForm, NoFreeMiniInvoiceForm, TypePrice, Invoice
from django.contrib.auth.decorators import login_required
import json
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.utils import formats
from django.utils.dateformat import format
from django.db.models import Q
from doctor.models import Doctor
from agenda.models import Slot


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
    c = {'doctor': request.user.userprofile.current_doctor, 'slot_type': settings.SLOT_TYPE,
         'slottemplates': request.user.userprofile.current_doctor.get_all_slottemplates(),
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
    doc = up.current_doctor
    c = {'userprofile_id': request.user.userprofile.id,
         'personal_data_form': DoctorForm(instance=doc),
         'settings_form': SettingsForm(instance=doc), 'avatar': doc.picture,
         'text_form': TextForm(instance=doc), 'color_forms': [],
         'password_change_form': PasswordChangeForm(user=request.user),
         'invoice': doc.get_active_invoice(),
         'new_invoice': MiniInvoiceForm() if not doc.already_use_free_invoice() else NoFreeMiniInvoiceForm()}
    for st in settings.SLOT_TYPE:
        d = {'id': doc.get_colorslot(st[0]).id, 'name': st[1],
             'form': ColorForm(instance=doc.get_colorslot(st[0]))}
        c['color_forms'].append(d)
    return render(request, 'config.tpl', c)


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
    for i in request.user.userprofile.current_doctor.invoices.all().order_by('id'):
        if i.paid:
            paid = format(i.date_paid, date_format)
        else:
            paid = '<a href="link/sofort" class="btn btn-danger" role="button">%s</a>' % _("Pay now")
        data.append([i.id, format(i.date_creation, date_format), i.type_price, format(i.date_start, date_format),
                     format(i.date_end, date_format), "%.2f euros" % i.price_incVAT, paid])
    c = {'title': 'Invoices', 'table': {'data': data, 'titles': titles}}
    return render(request, 'table.tpl', c)


def reminder(request, slug):
    if request.is_ajax():
        email = request.GET['email']
        s = get_object_or_404(Slot, refer_doctor__slug=slug, patient__mail=email)
        # s = Slot.objects.filter(refer_doctor__slug=slug, patient__mail=email)
        if s:
            # TODO SEND MAIL PATIENT_REMINDER
            return HttpResponse(json.dumps({'return': False}))
        else:
            return HttpResponse(json.dumps({'return': False}))