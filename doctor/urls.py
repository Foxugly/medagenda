# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from doctor.views import calendar_user, search_doctor, model_calendar, user_settings, personal_data, reminder_slot,\
    config, avatar, text_profil, color, remove_picture, reminder, invoice_add, invoice_remove, invoices, profile
urlpatterns = (
    url(r'^settings/$', login_required(user_settings), name='settings'),
    url(r'^invoice/$', login_required(invoices), name='invoice'),
    url(r'^calendar/$', login_required(calendar_user), name='calendar'),
    url(r'^calendar/(?P<slug>[\w-]+)/$', calendar_user, name='calendar_user'),
    url(r'^model/$', login_required(model_calendar), name='model'),
    url(r'^ajax/reminder/(?P<slug>[\w-]+)/$', reminder, name='reminder'),
    url(r'^reminder/(?P<slug>[\w-]+)/$', reminder_slot, name='reminder_slot'),
    url(r'^ajax/personal_data/$', login_required(personal_data), name="personal_data"),
    url(r'^ajax/config/$', login_required(config), name="config"),
    url(r'^ajax/avatar/$', login_required(avatar), name="avatar"),
    url(r'^ajax/text/$', login_required(text_profil), name="text"),
    url(r'^ajax/color/(?P<color_id>[\w-]+)/$', login_required(color), name="color"),
    url(r'^ajax/remove_picture/$', login_required(remove_picture), name="remove_picture"),
    url(r'^ajax/search/$', search_doctor, name='search_doctor'),
    url(r'^ajax/invoice/add/$', invoice_add, name='invoice_add'),
    url(r'^ajax/invoice/remove/(?P<invoice_id>[\w-]+)/$', invoice_remove, name='invoice_remove'),
    url(r'^(?P<slug>[\w-]+)/$', profile, name='profile'),
)
