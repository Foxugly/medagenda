# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import patterns, url
from agenda.views import agenda_add, agenda_remove, agenda_apply

urlpatterns = (
    url(r'^ajax/(?P<slug>[\w-]+)/add/$', agenda_add, name='agenda_add'),
    url(r'^ajax/(?P<slug>[\w-]+)/remove/$', agenda_remove, name='agenda_remove'),
    url(r'^ajax/(?P<slug>[\w-]+)/apply/$', agenda_apply, name='agenda_apply'),
)
