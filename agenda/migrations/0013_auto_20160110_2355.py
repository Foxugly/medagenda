# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0012_slot_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slot',
            old_name='refer_doctor',
            new_name='refer_userprofile',
        ),
    ]
