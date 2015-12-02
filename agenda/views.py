# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from utils.perms import get_context
from datetime import datetime, timedelta
from django.conf import settings
from agenda.models import SlotTemplate
import json


@login_required
def agenda_add(request, slug):
    if request.is_ajax():
        user = get_context(request)['userprofile']
        days = ['check_monday', 'check_tuesday', 'check_wednesday', 'check_thursday', 'check_friday', 'check_saturday', 'check_sunday']
        results = {}
        for day in days:
            if day in request.GET:
                dt = user.get_daytemplate(days.index(day)+1)
                current = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.GET['start_time'], '%Y-%m-%d %H:%M')
                current += timedelta(days=days.index(day))
                end = datetime.strptime(settings.FULLCALENDAR_REF_DATE + ' ' + request.GET['end_time'], '%Y-%m-%d %H:%M')
                end += timedelta(days=days.index(day))
                while current < end:
                    current_end = current + timedelta(minutes=int(request.GET['duration']))
                    if dt.n_slottemplates() > 0:
                        print 'MANAGE OTHER SLOTS'  # TODO
                    pricing = False if request.GET['pricing'] == "1" else True
                    st = SlotTemplate(start=current, end=current_end, national_health_service_price=pricing)
                    st.save()
                    dt.add_slottemplate(st)
                    current = current_end + timedelta(minutes=int(request.GET['break_time']))
        results['slottemplates'] = user.get_all_slottemplates()
        return HttpResponse(json.dumps(results))


@login_required
def agenda_remove(request, slug):
    if request.is_ajax():
        user = get_context(request)['userprofile']
        user.remove_all_slottemplates()
        results = {}
        results['slottemplates'] = user.get_all_slottemplates()
        return HttpResponse(json.dumps(results))


@login_required
def agenda_apply(request, slug):
    if request.is_ajax():
        results = {}
        # TODO
        # results = [y.as_json() for y in c.years.filter(active=True)]
        return HttpResponse(json.dumps(results))
