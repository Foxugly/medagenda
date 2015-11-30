# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151129_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='view_busy_slot',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'pic', blank=True),
        ),
    ]
