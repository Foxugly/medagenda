# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import os
import random
import string
import tempfile
from icalendar import vText, Event, Calendar
from datetime import datetime
import pytz
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def string_random(size):
    s = string.lowercase + string.uppercase + string.digits
    return ''.join(random.sample(s, size))


def mail():
    return None


def calendar(s):
    cal = Calendar()
    cal.add('version', '2.0')
    cal.add('prodid', '-//Medical consultation//')
    cal.add('calscale', 'GREGORIAN')
    cal.add('method', 'PUBLISH')
    cal.add('x-wr-calname', '[Medagenda] Consultation')
    cal.add('x-wr-timezone', s.refer_doctor.timezone)
    cal.add('x-wr-caldesc', '')

    event = Event()
    title = '[Medical consultation] %s' % str(s.refer_doctor.full_name())
    event.add('dtstart', s.start_dt())
    event.add('dtend', s.end_dt())
    event.add('dtstamp', datetime.now(pytz.timezone(str(s.refer_doctor.timezone))))
    event.add('created', datetime.now(pytz.timezone(str(s.refer_doctor.timezone))))
    event['description'] = vText(_(u"Medical consultation with %s" % s.refer_doctor.full_name()))
    event.add('last-modified', datetime.now(pytz.timezone(str(s.refer_doctor.timezone))))
    event['location'] = vText(s.refer_doctor.address.formatted)
    event.add('sequence', 0)
    event['status'] = vText('CONFIRMED')
    event.add('summary', title)
    event['transp'] = vText('OPAQUE')
    cal.add_component(event)
    directory = tempfile.mkdtemp()
    f = open(os.path.join(directory, 'example.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()
    f2 = open(os.path.join(settings.MEDIA_ROOT, 'ics', s.refer_doctor.slug+'.ics'), 'wb')
    f2.write(cal.to_ical())
    f2.close()
    print os.path.join(directory, 'example.ics')
    return cal


def reformat_date(s):
    out = s
    out = out.replace('yyyy', '%Y')
    out = out.replace('yy', '%y')
    out = out.replace('mm', '%m')
    out = out.replace('dd', '%d')
    return out
