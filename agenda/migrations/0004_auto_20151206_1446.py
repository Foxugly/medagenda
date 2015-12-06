# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20151206_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='slot_template',
            new_name='st',
        ),
    ]
