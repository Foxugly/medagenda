# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='refer_userprofile',
            field=models.ForeignKey(related_name='back_userprofile', verbose_name='UserProfile', to='users.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='st',
            field=models.ForeignKey(verbose_name='Slot template', blank=True, to='agenda.SlotTemplate', null=True),
        ),
        migrations.AddField(
            model_name='daytemplate',
            name='slots',
            field=models.ManyToManyField(to='agenda.SlotTemplate', verbose_name='Slots', blank=True),
        ),
    ]
