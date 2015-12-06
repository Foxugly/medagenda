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
from agenda.models import SlotTemplate, Slot
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
                        for old_slot in dt.slots.filter(start__lte=current, end__gt=current):
                            dt.slots.remove(old_slot)
                        for old_slot in dt.slots.filter(start__lt=current_end, end__gte=current_end):
                            dt.slots.remove(old_slot)  
                    pricing = False if request.GET['pricing'] == "1" else True
                    st = SlotTemplate(start=current, end=current_end, national_health_service_price=pricing)
                    st.save()
                    dt.add_slottemplate(st)
                    current = current_end + timedelta(minutes=int(request.GET['break_time']))
        results['return'] = True
        results['slottemplates'] = user.get_all_slottemplates()
        return HttpResponse(json.dumps(results))


@login_required
def agenda_remove(request, slug):
    if request.is_ajax():
        user = get_context(request)['userprofile']
        user.remove_all_slottemplates()
        results = {}
        results['slottemplates'] = user.get_all_slottemplates()
        results['return'] = True
        return HttpResponse(json.dumps(results))


@login_required
def agenda_apply(request, slug):
    if request.is_ajax():
        if 'start_date' in request.GET and 'end_date' in request.GET :
            user = get_context(request)['userprofile']
            results = {}
            format_date = request.GET['format']
            format_date = format_date.replace('yyyy','%Y')
            format_date = format_date.replace('mm','%m')
            format_date = format_date.replace('dd','%d')
            start_date = datetime.strptime(request.GET['start_date'], format_date)
            end_date = datetime.strptime(request.GET['end_date'], format_date)
            ref_date = datetime.strptime(settings.FULLCALENDAR_REF_DATE , settings.FULLCALENDAR_REF_DATEFORMAT)
            for i in range(0,7): #datetime.weekday() #0 = Monday - 6= Sunday
                ref_day = ref_date + timedelta(days=(int(start_date.weekday()) + i))
                current_day = start_date + timedelta(days=i)
                while current_day <= end_date :
                    sts = user.weektemplate.get_slottemplates_of_day(1+(int(start_date.weekday()) + i)%7)
                    if sts :
                        for st in sts :
                            current_day = current_day.replace(hour=st.start.hour, minute=st.start.minute)
                            for s in user.slots.filter(date=datetime.date(current_day),st__start__lt=current_day, st__start__gt=current_day):
                                user.slots.remove(s)
                            current_day = current_day.replace(hour=st.end.hour, minute=st.end.minute)
                            for s in user.slots.filter(date=datetime.date(current_day), st__end__lt=current_day, st__end__gt=current_day):
                                user.slots.remove(s)
                            new_slot = Slot(date=datetime.date(current_day), st=st, refer_doctor=user)
                            new_slot.save()
                            user.slots.add(new_slot)
                    current_day += timedelta(days=7)
            results['return'] = True
        else :
            results['return'] = False
        return HttpResponse(json.dumps(results))
