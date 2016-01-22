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
from users.views import add_user, create_user, password, collaborator_add

urlpatterns = (
    url(r'^login/$', views.login, {'template_name': 'login.tpl'}, name='login'),
    url(r'^logout/$', login_required(views.logout), {'template_name': 'logout.tpl'}, name='logout'),
    url(r'^add_user/$', add_user, name='add_user'),
    url(r'^create_user/$', create_user, name='create_user'),
    url(r'^collaborator/add/(?P<collaborator_id>\w+)/(?P<confirm>\w+)/$', collaborator_add, name='collaborator_add'),
    url(r'^password/reset/$', views.password_reset, {'template_name': 'password_reset_form.tpl'}, name="password_reset"),
    url(r'^password/reset/done/$', views.password_reset_done, {'template_name': 'password_reset_done.tpl'},
        name="password_reset_done"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.password_reset_confirm,
        {'template_name': 'password_reset_confirm.tpl'}, name="password_reset_confirm"),
    url(r'^password/done/$', views.password_reset_complete, {'template_name': 'password_reset_complete.tpl'},
        name="password_reset_complete"),
    url(r'^ajax/password/$', login_required(password), name='password'),
)
