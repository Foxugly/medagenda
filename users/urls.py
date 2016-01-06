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
from django.contrib.auth import views
from users.views import add_user, calendar_user, search_doctor, model_calendar, user_settings, create_user, personal_data, \
    config, avatar, text, color, remove_picture, password, invoice_add, invoice_remove, invoices

urlpatterns = (
    url(r'^login/$', views.login, {'template_name': 'login.tpl'}, name='login'),
    url(r'^logout/$', login_required(views.logout), {'template_name': 'logout.tpl'}, name='logout'),
    url(r'^add_user/$', add_user, name='add_user'),
    url(r'^create_user/$', create_user, name='create_user'),
    url(r'^settings/$', login_required(user_settings), name='settings'),
    url(r'^password/reset/$', views.password_reset, {'template_name': 'password_reset_form.tpl'}, name="password_reset"),
    url(r'^password/reset/done/$', views.password_reset_done, {'template_name': 'password_reset_done.tpl'},
        name="password_reset_done"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm,
        {'template_name': 'password_reset_confirm.tpl'}, name="password_reset_confirm"),
    url(r'^password/done/$', views.password_reset_complete, {'template_name': 'password_reset_complete.tpl'},
        name="password_reset_complete"),
    url(r'^invoice/$', login_required(invoices), name='invoice'),
    url(r'^calendar/$', login_required(calendar_user), name='calendar'),
    url(r'^model/$', login_required(model_calendar), name='model'),
    url(r'^ajax/personal_data/$', login_required(personal_data), name="personal_data"),
    url(r'^ajax/config/$', login_required(config), name="config"),
    url(r'^ajax/avatar/$', login_required(avatar), name="avatar"),
    url(r'^ajax/text/$', login_required(text), name="text"),
    url(r'^ajax/color/(?P<color_id>[\w-]+)/$', login_required(color), name="color"),
    url(r'^ajax/remove_picture/$', login_required(remove_picture), name="remove_picture"),
    url(r'^ajax/search/$', search_doctor, name='search_doctor'),
    url(r'^ajax/invoice/add/$', invoice_add, name='invoice_add'),
    url(r'^ajax/invoice/remove/(?P<invoice_id>[\w-]+)/$', invoice_remove, name='invoice_remove'),
    url(r'^ajax/password/$', login_required(password), name='password'),
)
