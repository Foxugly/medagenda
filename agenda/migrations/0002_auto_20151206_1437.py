# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytemplate',
            name='slots',
            field=models.ManyToManyField(to='agenda.SlotTemplate', verbose_name='Slots', blank=True),
        ),
        migrations.AlterField(
            model_name='slottemplate',
            name='national_health_service_price',
            field=models.BooleanField(verbose_name='National health service pricing'),
        ),
        migrations.AlterField(
            model_name='weektemplate',
            name='days',
            field=models.ManyToManyField(to='agenda.DayTemplate', verbose_name='Days', blank=True),
        ),
    ]
