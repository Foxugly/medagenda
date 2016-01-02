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
from users.views import add_user, calendar_user, search_doctor, model_calendar, update_user, create_user, personal_data, \
    config, avatar, text, color, remove_picture, password, invoice_add, invoice_remove

urlpatterns = (
    url(r'^login/$', views.login, {'template_name': 'login.tpl'}),
    url(r'^logout/$', login_required(views.logout), {'template_name': 'logout.tpl'}, name='logout'),
    url(r'^add_user/$', add_user, name='add_user'),
    url(r'^create_user/$', create_user, name='create_user'),
    url(r'^settings/$', login_required(update_user), name='update_user'),

    # url(r'^password_reset/$', login_required(views.password_reset), name='password_reset'),
    # url(r'^password_reset/done/$', login_required(views.password_reset_done), name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # login_required(views.password_reset_confirm), name='password_reset_confirm'),
    # url(r'^reset/done/$', login_required(views.password_reset_complete), name='password_reset_complete'),

    # TODO finaliser le nouveau mot de passe
    url(r'^password/reset/$', views.password_reset,
        {'post_reset_redirect': '/user/password/reset/done/', 'template_name': 'form.tpl'}, name="password_reset"),
    url(r'^password/reset/done/$', views.password_reset_done, {'template_name': 'form.tpl'},
        name="password_reset_done"),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm,
        {'post_reset_redirect': '/user/password/done/', 'template_name': 'form.tpl'}),
    url(r'^password/done/$', views.password_reset_complete, {'template_name': 'form.tpl'}),

    # url(r'^calendar/(?P<slug>[\w-]+)/$', calendar_user, name='calendar_user'),
    url(r'^calendar/$', login_required(calendar_user), name='calendar_user2'),
    url(r'^model/$', login_required(model_calendar), name='model_calendar'),
    # url(r'^reminder/(?P<slug>[\w-]+)/$', reminder_slot, name='reminder_slot'),
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
    # url(r'^(?P<slug>[\w-]+)/$', profile, name='profile'),

)
