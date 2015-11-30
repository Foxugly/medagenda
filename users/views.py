# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.


from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import json
from users.models import UserProfile, UserProfileForm
from utils.perms import get_context
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

def home(request):
    if request.user.is_authenticated():
        # doctors
        if request.user.is_superuser:
            # admin
            userprofiles = UserProfile.objects.all()
            c = get_context(request)
            c['list'] = userprofiles
            return render_to_response('list.tpl', c)
    else :
        userprofiles = UserProfile.objects.all()
        c = get_context(request)
        c['list'] = userprofiles
        return render_to_response('list.tpl', c)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    c = get_context(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print('VALID')
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Error")
            print('ERROR1')
    else:
        messages.error(request, "Error")
        print('ERROR2')
        c['form'] = UserProfileForm()
        c['url'] = "/user/adduser/"
        c['title'] = _("New doctor")
    return render(request, 'form.tpl', c)