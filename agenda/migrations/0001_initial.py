# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151130_0236'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.IntegerField(choices=[(1, 'Lundi'), (2, 'Mardi'), (3, 'Mercredi'), (4, 'Jeudi'), (5, 'Vendredi'), (6, 'Samedi'), (7, 'Dimanche')])),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(blank=True, to='patient.Patient', null=True)),
                ('refer_doctor', models.ForeignKey(related_name='back_userprofile', verbose_name='UserProfile', to='users.UserProfile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlotTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.TimeField(verbose_name='D\xe9but')),
                ('end', models.TimeField(verbose_name='Fin')),
                ('national_health_service_price', models.BooleanField(verbose_name='Tarif Conventionn\xe9')),
            ],
        ),
        migrations.CreateModel(
            name='WeekTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('days', models.ManyToManyField(to='agenda.DayTemplate', verbose_name='Jours', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='slotTemplate',
            field=models.ForeignKey(blank=True, to='agenda.SlotTemplate', null=True),
        ),
        migrations.AddField(
            model_name='daytemplate',
            name='slots',
            field=models.ManyToManyField(to='agenda.SlotTemplate', verbose_name='Cr\xe9neaux Horaires', blank=True),
        ),
    ]
