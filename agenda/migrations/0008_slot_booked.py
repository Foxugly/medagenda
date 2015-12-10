# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_auto_20151208_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='booked',
            field=models.BooleanField(default=False, verbose_name='Patient'),
        ),
    ]
