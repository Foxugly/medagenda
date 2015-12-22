# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import url
from patient.views import search_patient, confirm_create, confirm_remove, reminder

urlpatterns = (
    url(r'^ajax/search/$', search_patient, name='search_patient'),
    url(r'^confirm/create/(?P<patient_id>[\w-]+)/(?P<txt>[\w-]+)/$', confirm_create, name='confirm_create'),
    url(r'^confirm/remove/(?P<patient_id>[\w-]+)/(?P<slot_id>[\w-]+)/$', confirm_remove, name='confirm_remove'),
    url(r'^ajax/reminder/(?P<slug>[\w-]+)/$', reminder, name='reminder'),
)
