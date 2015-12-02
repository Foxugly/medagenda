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
import json

@login_required
def agenda_add(request,slug):
	if request.is_ajax():
		user = get_context(request)['userprofile']
		if 'check_monday' in request.GET:
			print request.GET['check_monday']
		print request.GET['start_time']
		print request.GET['end_time']
		print request.GET['duration']
		print request.GET['break_time']
		print request.GET['pricing']
		results = {}
		results['ok']='true'
		results['slots']=[]
		# results = [y.as_json() for y in c.years.filter(active=True)]
		for day in user.weektemplate.days.all():
			for s in day.slots.all():
				results['slots'].append(s.as_json(day.day,user))
		print results
		return HttpResponse(json.dumps(results))

@login_required
def agenda_remove(request,slug):
	if request.is_ajax():
		results = {}
		results['ok']='true'
		# results = [y.as_json() for y in c.years.filter(active=True)]
		return HttpResponse(json.dumps(results))

@login_required
def agenda_apply(request,slug):
	if request.is_ajax():
		results = {}
		results['ok']='true'
		# results = [y.as_json() for y in c.years.filter(active=True)]
		return HttpResponse(json.dumps(results))