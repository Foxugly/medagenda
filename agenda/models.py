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
# Create your models here.
from patient.models import Patient
from datetime import datetime, timedelta

class SlotTemplate(models.Model):
    start = models.TimeField(verbose_name=_(u'Début'), blank=False)
    end = models.TimeField(verbose_name=_(u'Fin'), blank=False)
    national_health_service_price = models.BooleanField(verbose_name=_(u"Tarif Conventionné"))

    def __str__(self):
        pricing = _(u"Tarif Conventionne") if self.national_health_service_price else _(u'Tarif libre')
        return u"%s - %s (%s)" %(self.start, self.end, pricing)

    def t_start(self,i):
        date = datetime.strptime(settings.FULLCALENDAR_REF_DATE, "%Y-%m-%d")
        date += timedelta(days=(i-1))
        return str(date.strftime('%Y-%m-%d')) + str('T') + str(self.start)


    def t_end(self,i):
        date = datetime.strptime(settings.FULLCALENDAR_REF_DATE, "%Y-%m-%d")
        date += timedelta(days=(i-1))
        return str(date.strftime('%Y-%m-%d')) + str('T') + str(self.end)

    def as_json(self,i,doctor):
        if self.national_health_service_price:
            color = str(doctor.nhs_price_free_slot_color)
        else:
            color = str(doctor.free_price_free_slot_color)
        return dict(id=self.id, start=self.t_start(i), end=self.t_end(i), title=str(_('Libre')),color=color) 

# use date.isoweekday()
class DayTemplate(models.Model):
    day = models.IntegerField(choices=settings.DAY_CHOICES)
    slots = models.ManyToManyField(SlotTemplate, verbose_name=_(u'Créneaux Horaires'), blank=True)

    def add_slots(self, slot):
        if slot not in self.slots:
            self.slots.add(slot)

    def remove_slots(self,slot):
        if slot in self.slots:
            del self.slots[slot]

    def n_slots(self):
        return len(self.slots)

    def __str__(self):
         return u"[%d] %s" % (self.id, dict(settings.DAY_CHOICES)[self.day])


class WeekTemplate(models.Model):
    days = models.ManyToManyField(DayTemplate, verbose_name=_(u'Jours'), blank=True)

    def add_daytemplate(self,dt):
        self.remove_day(dt.day)
        self.days.add(day)

    def remove_daytemplate(self, dt):
        for d in self.days.all():
            if d == dt:
                del self.days.d

    def remove_day(self,d):
        for d in self.days.all():
            if d.day == d:
                del self.days.d

    def __str__(self):
        return u"WeekTemplate %d" % self.id

class Slot(models.Model):
    date = models.DateField()
    slotTemplate = models.ForeignKey(SlotTemplate, blank=True, null=True)
    patient = models.ForeignKey(Patient, blank=True, null=True)
    refer_doctor = models.ForeignKey('users.UserProfile', verbose_name=_('UserProfile'), related_name="back_userprofile", null=True)

    def start(self):
        return self.date.strftime('%Y-%m-%d') + "T" + self.slotTemplate.start.strftime('%H:%M:%S')

    def end(self):
        return self.date.strftime('%Y-%m-%d') + "T" + self.slotTemplate.end.strftime('%H:%M:%S')

    def as_json(self):
        # nhsp=self.slotTemplate.national_health_service_price
        color = 'black'
        if self.patient :
            if refer_doctor.view_busy_slot :
                if self.slotTemplate.national_health_service_price:
                    color = str(self.refer_doctor.nhs_price_booked_slot_color)
                else:
                    color = str(self.refer_doctor.free_price_booked_slot_color)
                return dict(id=self.id, start=self.start(), end=self.end(), title=str(_('Réservé')),color=color)     
            else:
                return None
        else:
            if self.slotTemplate.national_health_service_price:
                color = str(self.refer_doctor.nhs_price_free_slot_color)
            else:
                color = str(self.refer_doctor.free_price_free_slot_color)
            return dict(id=self.id, start=self.start(), end=self.end(), title=str(_('Libre')),color=color)      

    def __str__(self):
        return u"slot %d" % self.id