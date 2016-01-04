# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from patient.models import Patient
from django.http import HttpResponse
import json
from agenda.models import Slot
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404


def search_patient(request):
    if request.is_ajax():
        email = request.GET['email']
        print email
        if len(email) > 5:
            p = Patient.objects.filter(email=email)
            if len(p):
                return HttpResponse(json.dumps({'return': True, 'patient': p[0].as_json()}))
            else:
                return HttpResponse(json.dumps({'return': False}))
        else:
            return HttpResponse(json.dumps({'return': False}))


def reminder(request, slug):
    if request.is_ajax():
        email = request.GET['email']
        s = get_object_or_404(Slot,refer_doctor__slug=slug, patient__mail=email )
        # s = Slot.objects.filter(refer_doctor__slug=slug, patient__mail=email)
        if s:
            #TODO SEND MAIL PATIENT_REMINDER
            print str(s.patient.email) + ' : ' + settings.WEBSITE_URL + '/patient/confirm/remove/' + str(s.patient.id) + '/' + str(s.id) + '/'
            return HttpResponse(json.dumps({'return': False}))
        else:
            return HttpResponse(json.dumps({'return': False}))


def confirm_create(request, patient_id, text):
    p = get_object_or_404(Patient, id=patient_id, confirm=text)
    if p:
        p.active = True
        p.confirm = None
        p.save()
        return render(request, 'valid.tpl')


def confirm_remove(request, patient_id, slot_id):
    s = get_object_or_404(Slot, id=slot_id, patient__id=patient_id)
    # s = Slot.objects.get(id=slot_id, patient__id=patient_id)
    # TODO SEND MAIL PATIENT_REMOVE_BOOKING
    s.clean_slot()
    s.save()
    return render(request, 'valid.tpl')

