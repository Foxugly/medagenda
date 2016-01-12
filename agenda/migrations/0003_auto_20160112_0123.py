# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20160111_2302'),
        ('agenda', '0002_auto_20160111_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='refer_userprofile',
        ),
        migrations.AddField(
            model_name='slot',
            name='refer_doctor',
            field=models.ForeignKey(related_name='back_doctor', verbose_name='refer_doctor', to='doctor.Doctor', null=True),
        ),
    ]
