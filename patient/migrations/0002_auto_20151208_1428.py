# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='mail',
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='information',
            field=models.TextField(null=True, verbose_name='Informations utiles', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last_name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='Telephone'),
        ),
    ]
