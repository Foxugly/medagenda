# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import patterns, url
from agenda.views import st_add, st_remove, st_apply, st_clean, get_slot, book_slot, remove_slot, clean_slot
from django.contrib.auth.decorators import login_required

urlpatterns = (
    url(r'^ajax/s/get/(?P<slot_id>[\w-]+)/$', get_slot, name='get_slot'),
    url(r'^ajax/st/add/$', login_required(st_add), name='st_add'),
    url(r'^ajax/st/clean/$', login_required(st_clean), name='st_clean'),
    url(r'^ajax/st/apply/$', login_required(st_apply), name='st_apply'),
    url(r'^ajax/st/remove/(?P<st_id>\w+)/$', login_required(st_remove), name='st_remove'),
    url(r'^ajax/s/book/(?P<slot_id>[\w-]+)/$', book_slot, name='book_slot'),
    url(r'^ajax/s/remove/(?P<slot_id>[\w-]+)/$', login_required(remove_slot), name='remove_slot'),
    url(r'^ajax/s/clean/(?P<slot_id>[\w-]+)/$', login_required(clean_slot), name='clean_slot'),
)
