# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20160111_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
