# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151201_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='end_time',
            field=models.TimeField(default=b'18:00:00'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='start_time',
            field=models.TimeField(default=b'09:00:00'),
        ),
    ]
