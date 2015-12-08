# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20151208_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='informations',
            field=models.TextField(null=True, verbose_name='Usefull informations', blank=True),
        ),
    ]
