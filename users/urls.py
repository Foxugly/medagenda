# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from users.views import add_user, profile_user, calendar_user, reminder_slot, remove_slot, find_slot, model_calendar, config_user

urlpatterns = (
    url(r'^adduser/$', add_user, name='add_user'),
    url(r'^config/$', config_user, name='config_user'),
    url(r'^(?P<slug>[\w-]+)/$', profile_user, name='profile_user'),
    url(r'^(?P<slug>[\w-]+)/calendar/$', calendar_user, name='calendar_user'),
    url(r'^(?P<slug>[\w-]+)/model/$', login_required(model_calendar), name='model_calendar'),
    url(r'^(?P<slug>[\w-]+)/reminder/$', reminder_slot, name='reminder_user'),
    url(r'^login/$', views.login, {'template_name': 'login.tpl'}),
    url(r'^logout/$', login_required(views.logout), {'template_name': 'logout.tpl'}, name='logout'),
    url(r'^password_change/$', login_required(views.password_change), name='password_change'),
    url(r'^password_change/done/$', login_required(views.password_change_done), name='password_change_done'),
    url(r'^password_reset/$', login_required(views.password_reset), name='password_reset'),
    url(r'^password_reset/done/$', login_required(views.password_reset_done), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        login_required(views.password_reset_confirm), name='password_reset_confirm'),
    url(r'^reset/done/$', login_required(views.password_reset_complete), name='password_reset_complete'),
)
