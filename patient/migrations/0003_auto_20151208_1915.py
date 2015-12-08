# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20151208_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='information',
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=100, null=True, verbose_name='First name', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Last_name', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telephone', blank=True),
        ),
    ]
