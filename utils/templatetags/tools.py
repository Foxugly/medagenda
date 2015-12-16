# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django import template
import os

register = template.Library()


@register.filter()
def index(d, value):
    return dict(d)[value]


@register.filter()
def time_format(time):
    return u"%d:%d" % (time.hour, time.minute)


@register.filter()
def filename(path):
    return os.path.basename(path.name)
