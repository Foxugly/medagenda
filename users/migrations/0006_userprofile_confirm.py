# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20151201_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='confirm',
            field=models.TextField(null=True, blank=True),
        ),
    ]
