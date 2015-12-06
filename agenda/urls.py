# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import patterns, url
from agenda.views import st_add, st_remove, st_apply, st_clean

urlpatterns = (
    url(r'^ajax/(?P<slug>[\w-]+)/st/add/$', st_add, name='st_add'),
    url(r'^ajax/(?P<slug>[\w-]+)/st/clean/$', st_clean, name='st_clean'),
    url(r'^ajax/(?P<slug>[\w-]+)/st/apply/$', st_apply, name='st_apply'),
    url(r'^ajax/(?P<slug>[\w-]+)/st/remove/(?P<st_id>\w+)/$', st_remove, name='st_remove'),
)
