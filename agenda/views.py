# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.conf import settings
from agenda.models import SlotTemplate, Slot
from patient.models import Patient
import json


@login_required
def st_add(request):
    if request.is_ajax():
        days = ['check_monday', 'check_tuesday', 'check_wednesday', 'check_thursday', 'check_friday', 'check_saturday', 'check_sunday']
        results = {}
        for day in days:
            if day in request.GET:
                dt = request.user.userprofile.get_daytemplate(days.index(day)+1)
                current = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.GET['start_time'], '%Y-%m-%d %H:%M')
                current += timedelta(days=days.index(day))
                end = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.GET['end_time'], '%Y-%m-%d %H:%M')
                end += timedelta(days=days.index(day))
                while current < end:
                    current_end = current + timedelta(minutes=int(request.GET['duration']))
                    if dt.n_slottemplates() > 0:
                        for old_slot in dt.slots.filter(start__lte=current, end__gt=current):
                            dt.slots.remove(old_slot)
                        for old_slot in dt.slots.filter(start__lt=current_end, end__gte=current_end):
                            dt.slots.remove(old_slot)
                    booked = True if request.GET['booked'] == "1" else False
                    st = SlotTemplate(start=current, end=current_end, slot_type=request.GET['slot_type'],booked=booked)
                    st.save()
                    dt.add_slottemplate(st)
                    current = current_end + timedelta(minutes=int(request.GET['break_time']))
        results['return'] = True
        results['slottemplates'] = request.user.userprofile.get_all_slottemplates()
        return HttpResponse(json.dumps(results))


@login_required
def st_clean(request):
    if request.is_ajax():
        request.user.userprofile.remove_all_slottemplates()
        results = {}
        results['slottemplates'] = request.user.userprofile.get_all_slottemplates()
        results['return'] = True
        return HttpResponse(json.dumps(results))


@login_required
def st_apply(request):
    results = {}
    if request.is_ajax():
        if 'start_date' in request.GET and 'end_date' in request.GET:
            results = {}
            format_date = request.GET['format']
            format_date = format_date.replace('yyyy', '%Y')
            format_date = format_date.replace('mm', '%m')
            format_date = format_date.replace('dd', '%d')
            start_date = datetime.strptime(request.GET['start_date'], format_date)

            end_date = datetime.strptime(request.GET['end_date'], format_date)
            ref_date = datetime.strptime(settings.FULLCALENDAR_REF_DATE, settings.FULLCALENDAR_REF_DATEFORMAT)
            for i in range(0, 7):  # datetime.weekday() #0 = Monday - 6= Sunday
                ref_day = ref_date + timedelta(days=(int(start_date.weekday()) + i))
                current_day = start_date + timedelta(days=i)
                while current_day <= end_date:
                    sts = request.user.userprofile.get_daytemplate(1+(int(start_date.weekday()) + i) % 7).get_slottemplates()
                    if sts:
                        for st in sts:
                            current_day = current_day.replace(hour=st.start.hour, minute=st.start.minute)
                            for s in request.user.userprofile.slots.filter(date=datetime.date(current_day), st__start__lte=current_day, st__end__gt=current_day):
                                request.user.userprofile.slots.remove(s)
                            current_day = current_day.replace(hour=st.end.hour, minute=st.end.minute)
                            for s in request.user.userprofile.slots.filter(date=datetime.date(current_day), st__start__lt=current_day, st__end__gte=current_day):
                                request.user.userprofile.slots.remove(s)
                            new_slot = Slot(date=datetime.date(current_day), st=st, refer_doctor=request.user.userprofile, booked=st.booked)
                            new_slot.save()
                            request.user.userprofile.slots.add(new_slot)
                    current_day += timedelta(days=7)
            results['return'] = True
        else:
            results['return'] = False
        return HttpResponse(json.dumps(results))


@login_required
def st_remove(request, st_id):
    results = {}
    if request.is_ajax():
        st = SlotTemplate.objects.get(id=int(st_id))
        for dt in request.user.userprofile.weektemplate.days.all():
            dt.remove_slottemplate(st)
        results['return'] = True
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


def get_slot(request, slot_id):
    results = {}
    if request.is_ajax():
        s = Slot.objects.get(id=int(slot_id))
        if request.user.is_authenticated():
            results['slot'] = s.detail()
            results['return'] = True
        else:
            if not s.patient :
                results['return'] = True
                results['slot'] = s.detail()
            else:
                results['return'] = False
    else:
        results['return'] = False
    return HttpResponse(json.dumps(results))


def book_slot(request, slot_id):
    if request.is_ajax():
        s = Slot.objects.get(id=slot_id)
        if request.GET["patient"] is None or int(request.GET["patient"]) == 0:
            #new Patient
            s.informations = request.GET["informations"]
            p = Patient(email=unicode(request.GET["email"]), first_name=unicode(request.GET["first_name"]), last_name=unicode(request.GET["last_name"]), telephone=unicode(request.GET["telephone"]))
            p.save()
            s.patient = p
            s.informations = unicode(request.GET["informations"])
        else :
            p = Patient.objects.get(id=int(request.GET["patient"]))
            s.patient = p
        s.booked = True
        s.save()
        d = {}
        d['return'] = True
        d['slot'] = s.as_json()
        return HttpResponse(json.dumps(d))

@login_required
def remove_slot(request, slot_id):
    if request.is_ajax():
        Slot.objects.get(id=slot_id).delete()
        return HttpResponse(json.dumps({'return':True}))

@login_required
def clean_slot(request, slot_id):
    if request.is_ajax():
        s = Slot.objects.get(id=slot_id)
        s.clean_slot()
        d = {}
        d['return'] = True
        d['slot'] = s.as_json()
        return HttpResponse(json.dumps(d))