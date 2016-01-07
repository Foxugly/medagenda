# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20160107_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2015, verbose_name='Year')),
                ('number', models.IntegerField(default=0, verbose_name='Number')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='path',
            field=models.CharField(max_length=255, null=True, verbose_name='path', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='can_recharge',
            field=models.BooleanField(default=True, verbose_name='Can recharge type of subscription '),
        ),
    ]
