# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160121_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='email_col',
            field=models.EmailField(max_length=254, verbose_name='Email address'),
        ),
    ]
