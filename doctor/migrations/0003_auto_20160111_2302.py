# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20160111_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='refer_userprofile',
            field=models.ForeignKey(related_name='refer_userprofile', verbose_name='UserProfile', blank=True, to='users.UserProfile', null=True),
        ),
    ]
