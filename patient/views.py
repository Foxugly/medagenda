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
