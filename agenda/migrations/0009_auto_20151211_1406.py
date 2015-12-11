# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_slot_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='booked',
            field=models.BooleanField(default=False, verbose_name='Booked'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='informations',
            field=models.TextField(null=True, verbose_name='Usefull informations', blank=True),
        ),
    ]
