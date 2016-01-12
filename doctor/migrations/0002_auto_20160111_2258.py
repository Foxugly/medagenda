# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20160111_2258'),
        ('users', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='refer_userprofile',
            field=models.ForeignKey(related_name='refer_userprofile', verbose_name='UserProfile', to='users.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='slots',
            field=models.ManyToManyField(to='agenda.Slot', verbose_name='Slots', blank=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='weektemplate',
            field=models.ForeignKey(verbose_name='Week template', blank=True, to='agenda.WeekTemplate', null=True),
        ),
    ]
