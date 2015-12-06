# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20151206_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='slotTemplate',
            new_name='slot_template',
        ),
    ]
