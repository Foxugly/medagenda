# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20160102_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=models.CharField(help_text='format : +32475123456', max_length=20, null=True, verbose_name='Telephone', blank=True),
        ),
    ]
