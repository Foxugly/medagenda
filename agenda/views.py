# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.conf import settings
from agenda.models import SlotTemplate, Slot
from patient.models import Patient
import json
from utils.toolbox import string_random
from utils.mail import mail_patient_welcome, mail_patient_cancel_appointment_from_doctor, mail_patient_new_appointment
from utils.toolbox import convert_date


@login_required
def st_add(request):
    if request.is_ajax():
        days = ['check_monday', 'check_tuesday', 'check_wednesday', 'check_thursday', 'check_friday', 'check_saturday',
                'check_sunday']
        results = {}
        for day in days:
            if day in request.POST:
                dt = request.user.userprofile.current_doctor.get_daytemplate(days.index(day) + 1)
                current = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.POST['start_time'],
                                            "%Y-%m-%d %H:%M")
                current += timedelta(days=days.index(day))
                end = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.POST['end_time'],
                                        '%Y-%m-%d %H:%M')
                end += timedelta(days=days.index(day))
                while current < end:
                    current_end = current + timedelta(minutes=int(request.POST['duration']))
                    if dt.n_slottemplates() > 0:
                        for old_slot in dt.slots.filter(start__lte=current, end__gt=current):
                            dt.slots.remove(old_slot)
                        for old_slot in dt.slots.filter(start__lt=current_end, end__gte=current_end):
                            dt.slots.remove(old_slot)
                    booked = True if request.POST['booked'] == "1" else False
                    st = SlotTemplate(start=current, end=current_end, slot_type=request.POST['slot_type'],
                                      booked=booked)
                    st.save()
                    dt.add_slottemplate(st)
                    current = current_end + timedelta(minutes=int(request.POST['break_time']))
        results['return'] = True
        results['slottemplates'] = request.user.userprofile.current_doctor.get_all_slottemplates()
        return HttpResponse(json.dumps(results))


@login_required
def st_clean(request):
    if request.is_ajax():
        request.user.userprofile.current_doctor.remove_all_slottemplates()
        results = {'slottemplates': request.user.userprofile.current_doctor.get_all_slottemplates(), 'return': True}
        return HttpResponse(json.dumps(results))


@login_required
def st_apply(request):
    results = {}
    if request.is_ajax():
        doc = request.user.userprofile.current_doctor
        if 'start_date' in request.POST and 'end_date' in request.POST:
            dateformat = request.POST['date_format']
            if not dateformat:
                dateformat = 'mm/dd/yyyy'
            dateformat = convert_date(dateformat)
            start_date = datetime.strptime(request.POST['start_date'], dateformat)
            end_date = datetime.strptime(request.POST['end_date'], dateformat)
            for i in range(0, 7):
                current_day = start_date + timedelta(days=i)
                while current_day <= end_date:
                    sts = doc.get_daytemplate(
                            1 + (int(start_date.weekday()) + i) % 7).get_slottemplates()
                    if sts:
                        for st in sts:
                            current_day = current_day.replace(hour=st.start.hour, minute=st.start.minute)
                            for s in doc.slots.filter(date=datetime.date(current_day), st__start__lte=current_day,
                                                      st__end__gt=current_day):
                                doc.slots.remove(s)
                            current_day = current_day.replace(hour=st.end.hour, minute=st.end.minute)
                            for s in doc.slots.filter(date=datetime.date(current_day), st__start__lt=current_day,
                                                      st__end__gte=current_day):
                                doc.slots.remove(s)
                            new_slot = Slot(date=datetime.date(current_day), st=st, refer_doctor=doc, booked=st.booked)
                            new_slot.save()
                            doc.slots.add(new_slot)
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
        for dt in request.user.userprofile.current_doctor.weektemplate.days.all():
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
            if not s.booked:
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
        if request.POST["patient"] is None or int(request.POST["patient"]) == 0:
            # new Patient
            s.informations = request.POST["informations"]
            p = Patient(email=unicode(request.POST["email"]), first_name=unicode(request.POST["first_name"]),
                        last_name=unicode(request.POST["last_name"]), telephone=unicode(request.POST["telephone"]))
            p.confirm = string_random(32)
            p.save()
            mail_patient_welcome(request, p)
            s.patient = p
            s.informations = unicode(request.POST["informations"])
        else:
            p = Patient.objects.get(id=int(request.POST["patient"]))
            s.patient = p
        s.booked = True
        s.save()
        s.icalendar()
        mail_patient_new_appointment(request, s)
        d = {'return': True, 'slot': s.as_json()}
        return HttpResponse(json.dumps(d))


@login_required
def remove_slot(request, slot_id):
    if request.is_ajax():
        slot = Slot.objects.get(id=slot_id)
        mail_patient_cancel_appointment_from_doctor(request, slot)
        slot.delete()
        return HttpResponse(json.dumps({'return': True}))


@login_required
def clean_slot(request, slot_id):
    if request.is_ajax():
        slot = Slot.objects.get(id=slot_id)
        mail_patient_cancel_appointment_from_doctor(request, slot)
        slot.clean_slot()
        d = {'return': True, 'slot': slot.as_json()}
        return HttpResponse(json.dumps(d))
