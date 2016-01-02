# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.conf.urls import url
from users.views import profile, calendar_user, reminder_slot

urlpatterns = (
    url(r'^calendar/(?P<slug>[\w-]+)/$', calendar_user, name='calendar_user'),
    url(r'^reminder/(?P<slug>[\w-]+)/$', reminder_slot, name='reminder_slot'),
    url(r'^(?P<slug>[\w-]+)/$', profile, name='profile'),

)
