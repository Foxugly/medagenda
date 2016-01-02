# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20151208_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Confirmed'),
        ),
        migrations.AddField(
            model_name='patient',
            name='confirm',
            field=models.TextField(null=True, verbose_name='Confirm key', blank=True),
        ),
    ]
