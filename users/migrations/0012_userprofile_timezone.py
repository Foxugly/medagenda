# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20151216_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default=b'Europe/Brussels'),
        ),
    ]
