# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from users.models import UserProfile
import random
import string

def get_context(request):
    c = {}
    if request.user.is_authenticated():
        c['userprofile'] = UserProfile.objects.get(user=request.user)
    return c

def string_random(size):
	s = string.lowercase + string.uppercase + string.digits
	return ''.join(random.sample(s,size))