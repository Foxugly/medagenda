# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20151206_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytemplate',
            name='day',
            field=models.IntegerField(verbose_name='Day', choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')]),
        ),
        migrations.AlterField(
            model_name='slot',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', blank=True, to='patient.Patient', null=True),
        ),
        migrations.AlterField(
            model_name='slot',
            name='st',
            field=models.ForeignKey(verbose_name='Slot template', blank=True, to='agenda.SlotTemplate', null=True),
        ),
        migrations.AlterField(
            model_name='slottemplate',
            name='end',
            field=models.TimeField(verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='slottemplate',
            name='start',
            field=models.TimeField(verbose_name='Start'),
        ),
    ]
