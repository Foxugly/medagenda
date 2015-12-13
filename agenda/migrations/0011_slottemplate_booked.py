# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_auto_20151212_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='slottemplate',
            name='booked',
            field=models.BooleanField(default=False, verbose_name='Booked'),
        ),
    ]
