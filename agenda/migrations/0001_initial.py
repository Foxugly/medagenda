# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(verbose_name='Day', choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')])),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('informations', models.TextField(null=True, verbose_name='Usefull informations', blank=True)),
                ('booked', models.BooleanField(default=False, verbose_name='Booked')),
                ('random', models.CharField(max_length=16, null=True, verbose_name='random character', blank=True)),
                ('path', models.CharField(max_length=255, null=True, verbose_name='path_ics', blank=True)),
                ('patient', models.ForeignKey(verbose_name='Patient', blank=True, to='patient.Patient', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlotTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField(verbose_name='Start')),
                ('end', models.TimeField(verbose_name='End')),
                ('slot_type', models.IntegerField(verbose_name='Slot type', choices=[(1, 'National Health Pricing Slot'), (2, 'Free Pricing Slot'), (3, 'Home visit Slot'), (4, 'Nursing home Slot')])),
                ('booked', models.BooleanField(default=False, verbose_name='Booked')),
            ],
        ),
        migrations.CreateModel(
            name='WeekTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('days', models.ManyToManyField(to='agenda.DayTemplate', verbose_name='Days', blank=True)),
            ],
        ),
    ]
