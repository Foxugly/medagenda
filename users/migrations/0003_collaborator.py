# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20160111_2302'),
        ('users', '0002_auto_20160112_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirm', models.TextField(null=True, verbose_name='Confirm key', blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('doctor', models.ForeignKey(blank=True, to='doctor.Doctor', null=True)),
            ],
        ),
    ]
