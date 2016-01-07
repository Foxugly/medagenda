# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_userprofile_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_creation',
            field=models.DateField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_paid',
            field=models.DateField(null=True, verbose_name='date paid', blank=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='type_price',
            field=models.ForeignKey(verbose_name='Type of subscription', to='users.TypePrice'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(blank=True, help_text='format : +32475123456', max_length=20, verbose_name='Telephone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
    ]
