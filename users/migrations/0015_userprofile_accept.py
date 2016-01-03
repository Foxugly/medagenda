# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20160102_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='accept',
            field=models.BooleanField(default=False, verbose_name='I accept the terms and conditions of use of Medagenda (see <a href="/conditions/"> here </a>)'),
        ),
    ]
