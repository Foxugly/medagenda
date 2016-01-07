# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_slottemplate_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='path',
            field=models.CharField(max_length=255, null=True, verbose_name='path_ics', blank=True),
        ),
    ]
