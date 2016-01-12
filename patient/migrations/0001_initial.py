# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True)),
                ('first_name', models.CharField(max_length=100, null=True, verbose_name='First name', blank=True)),
                ('last_name', models.CharField(max_length=100, null=True, verbose_name='Last_name', blank=True)),
                ('telephone', models.CharField(help_text='format : +32475123456', max_length=20, null=True, verbose_name='Telephone', blank=True)),
                ('active', models.BooleanField(default=False, verbose_name='Confirmed')),
                ('confirm', models.TextField(null=True, verbose_name='Confirm key', blank=True)),
            ],
        ),
    ]
