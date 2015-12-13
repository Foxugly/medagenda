# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_auto_20151211_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slottemplate',
            name='national_health_service_price',
        ),
        migrations.AddField(
            model_name='slottemplate',
            name='slot_type',
            field=models.IntegerField(default=1, verbose_name='Slot type', choices=[(1, 'National Health Pricing Slot'), (2, 'Free Pricing Slot'), (3, 'Home visit Slot'), (4, 'Nursing home Slot')]),
            preserve_default=False,
        ),
    ]
