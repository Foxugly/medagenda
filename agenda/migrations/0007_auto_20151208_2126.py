# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_slot_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='informations',
            field=models.TextField(null=True, verbose_name='Usefull informations+', blank=True),
        ),
    ]
