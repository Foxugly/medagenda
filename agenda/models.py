# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from patient.models import Patient
from datetime import datetime, timedelta
from utils.toolbox import reformat_date
import pytz


class SlotTemplate(models.Model):
    start = models.TimeField(verbose_name=_(u'Start'), blank=False)
    end = models.TimeField(verbose_name=_(u'End'), blank=False)
    slot_type = models.IntegerField(verbose_name=_(u'Slot type'), choices=settings.SLOT_TYPE)
    booked = models.BooleanField(verbose_name=_(u'Booked'), default=False)

    def __str__(self):
        return u"%s - %s (%s)" % (self.start, self.end, settings.SLOT_TYPE[self.slot_type])

    def t_start(self, i):
        date = datetime.strptime(settings.FULLCALENDAR_REF_DATE, "%Y-%m-%d")
        date += timedelta(days=(i - 1))
        return str(date.strftime('%Y-%m-%d')) + str('T') + str(self.start)

    def t_end(self, i):
        date = datetime.strptime(settings.FULLCALENDAR_REF_DATE, "%Y-%m-%d")
        date += timedelta(days=(i - 1))
        return str(date.strftime('%Y-%m-%d')) + str('T') + str(self.end)

    def get_title(self):
        return str(_('Booked') if self.booked else _('Free'))

    def as_json(self, i, doctor):
        return {'id': self.id, 'start': self.t_start(i), 'end': self.t_end(i), 'title': self.get_title(),
                'color': doctor.get_color(self.slot_type, self.booked)}


class DayTemplate(models.Model):
    day = models.IntegerField(verbose_name=_(u'Day'), choices=settings.DAY_CHOICES)
    slots = models.ManyToManyField(SlotTemplate, verbose_name=_(u'Slots'), blank=True)

    def add_slottemplate(self, st):
        if st not in self.slots.all():
            self.slots.add(st)

    def remove_slottemplate(self, st):
        if st in self.slots.all():
            self.slots.remove(st)

    def remove_all_slottemplates(self):
        for st in self.slots.all():
            self.remove_slottemplate(st)
            st.delete()

    def n_slottemplates(self):
        return len(self.slots.all())

    def get_slottemplates(self):
        return self.slots.all()

    def __str__(self):
        return u"[%d] %s" % (self.id, dict(settings.DAY_CHOICES)[self.day])


class WeekTemplate(models.Model):
    days = models.ManyToManyField(DayTemplate, verbose_name=_(u'Days'), blank=True)

    def add_daytemplate(self, dt):
        self.remove_day(dt.day)
        self.days.add(dt)

    def remove_daytemplate(self, dt):
        if dt in self.days.all():
            self.days.remove(dt)

    def remove_all_slottemplates(self):
        for dt in self.days.all():
            dt.remove_all_slottemplates()
            dt.delete()

    def remove_day(self, d):
        for dt in self.days.all():
            if dt.day == d:
                self.days.remove(dt)

    def get_daytemplate(self, i):
        daytmp = None
        if len(self.days.all()) > 0:
            for dt in self.days.all():
                if dt.day == i:
                    daytmp = dt
            if not daytmp:
                daytmp = DayTemplate(day=i)
                daytmp.save()
                self.add_daytemplate(daytmp)
        else:
            daytmp = DayTemplate(day=i)
            daytmp.save()
            self.add_daytemplate(daytmp)
        return daytmp

    def __str__(self):
        return u"WeekTemplate %d" % self.id


class Slot(models.Model):
    date = models.DateField(verbose_name=_(u'Date'))
    st = models.ForeignKey(SlotTemplate, verbose_name=_(u'Slot template'), blank=True, null=True)
    patient = models.ForeignKey(Patient, verbose_name=_(u'Patient'), blank=True, null=True)
    refer_doctor = models.ForeignKey('users.UserProfile', verbose_name=_('UserProfile'),
                                     related_name='back_userprofile', null=True)
    informations = models.TextField(verbose_name=_(u'Usefull informations'), blank=True, null=True)
    booked = models.BooleanField(verbose_name=_(u'Booked'), default=False)

    def clean_slot(self):
        self.patient = None
        self.booked = False
        self.save()

    def date_t(self, date_format):
        # return str(self.date.strftime('%d/%m/%Y'))
        return str(self.date.strftime(reformat_date(date_format)))

    @staticmethod
    def hour_t(t):
        return t.strftime('%H:%M:%S')

    def start_dt(self):
        tz = pytz.timezone(str(self.refer_doctor.timezone))
        return tz.localize(
            datetime(self.date.year, self.date.month, self.date.day, self.st.start.hour, self.st.start.minute, 0))

    def start_t(self):
        return self.date.strftime('%Y-%m-%d') + "T" + self.hour_t(self.st.start)

    def end_dt(self):
        tz = pytz.timezone(str(self.refer_doctor.timezone))
        return tz.localize(
            datetime(self.date.year, self.date.month, self.date.day, self.st.end.hour, self.st.end.minute, 0))

    def end_t(self):
        return self.date.strftime('%Y-%m-%d') + "T" + self.hour_t(self.st.end)

    def get_title(self):
        return str(_('Booked') if self.booked else _('Free'))

    def as_json(self):
        return dict(id=self.id, start=self.start_t(), end=self.end_t(), title=self.get_title(),
                    color=self.refer_doctor.get_color(self.st.slot_type, self.booked))

    #def as_json2(self):
    #    return dict(id=self.id, date=self.date_t(), start=self.hour_t(self.st.start))

    def detail(self, date_format=None):
        if self.booked:
            if self.refer_doctor.view_busy_slot:
                d = dict(id=self.id, date=self.date_t(date_format), start=self.hour_t(self.st.start), title=str(_('Booked')),
                         color=self.refer_doctor.get_color(self.st.slot_type, self.booked), booked=self.booked,
                         informations=self.informations)
                d_patient = self.patient.as_json()
                del d_patient['id']
                d.update(d_patient)
                return d
            else:
                return None
        else:
            return dict(id=self.id, date=self.date_t(date_format), start=self.hour_t(self.st.start), title=str(_('Free')),
                        color=self.refer_doctor.get_color(self.st.slot_type, self.booked))

    def __str__(self):
        return u"Slot %d" % self.id
