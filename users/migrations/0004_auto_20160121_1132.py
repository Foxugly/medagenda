# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_collaborator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaborator',
            old_name='email',
            new_name='email_col',
        ),
    ]
