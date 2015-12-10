# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151208_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='free_price_booked_slot_color',
            field=models.CharField(default=b'#F64636', max_length=8, verbose_name='Color free pricing booked'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='free_price_free_slot_color',
            field=models.CharField(default=b'#73B5EB', max_length=8, verbose_name='Color free pricing free'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nhs_price_booked_slot_color',
            field=models.CharField(default=b'#F64636', max_length=8, verbose_name='Color nhs pricing booked'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nhs_price_free_slot_color',
            field=models.CharField(default=b'#73EB79', max_length=8, verbose_name='Color nhs pricing free'),
        ),
    ]
