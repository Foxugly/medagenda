# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20151219_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Creation_date')),
                ('date_start', models.DateField(verbose_name='Start date')),
                ('date_end', models.DateField(verbose_name='End date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('price_exVAT', models.FloatField(default=0.0, verbose_name='Price excl. VAT')),
                ('VAT', models.FloatField(default=21, verbose_name='VAT (%)')),
                ('price_VAT', models.FloatField(default=0.0, verbose_name='Price VAT', blank=True)),
                ('price_incVAT', models.FloatField(default=0.0, verbose_name='Price inc. VAT', blank=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('date_paid', models.DateField(null=True, verbose_name='date Paid', blank=True)),
                ('note_paid', models.CharField(max_length=100, verbose_name='note paid', blank=True)),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
            ],
        ),
        migrations.CreateModel(
            name='TypePrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name='note paid', choices=[(1, 'Free'), (2, 'Standard'), (3, 'Premium')])),
                ('price_exVAT', models.IntegerField(verbose_name='exVAT price')),
                ('num_months', models.IntegerField(verbose_name='Number of months')),
                ('auto_extension', models.BooleanField(default=True, verbose_name='Auto Extension')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='type_price',
            field=models.ForeignKey(verbose_name='Type of account', to='users.TypePrice'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='invoices',
            field=models.ManyToManyField(to='users.Invoice', verbose_name='Invoices', blank=True),
        ),
    ]
