# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='current_doctor',
            field=models.ForeignKey(related_name='current_doctor', verbose_name='Current doctor', blank=True, to='doctor.Doctor', null=True),
        ),
    ]
