# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vat_number',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='speciality',
            field=models.CharField(max_length=10, choices=[(b'none', 'None'), (b'medgen', 'Medecine Generale'), (b'medint', 'Medecine Interne')]),
        ),
    ]
