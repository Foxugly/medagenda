# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import address.models
import timezone_field.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.IntegerField(verbose_name='Type of slot', choices=[(1, 'National Health Pricing Slot'), (2, 'Free Pricing Slot'), (3, 'Home visit Slot'), (4, 'Nursing home Slot')])),
                ('free_slot_color', models.CharField(default=b'#73B5EB', max_length=8, verbose_name='Free pricing free slot color')),
                ('booked_slot_color', models.CharField(default=b'#F64636', max_length=8, verbose_name='Booked slot color')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.IntegerField(verbose_name='Title', choices=[(1, 'Professeur'), (2, 'Docteur'), (3, 'Madame'), (4, 'Monsieur')])),
                ('picture', models.ImageField(null=True, upload_to=b'pic/', blank=True)),
                ('speciality', models.IntegerField(verbose_name='Speciality', choices=[(1, 'M\xe9decine G\xe9n\xe9rale'), (2, 'P\xe9diatrie'), (3, 'ORL'), (4, 'Cardiologue'), (5, 'Dentiste'), (13, 'Infirmier(\xe8re) ind\xe9pendant(e)'), (14, 'Kin\xe9sith\xe9rapeute'), (15, 'Ost\xe9opathe')])),
                ('slug', models.SlugField(verbose_name='slug', blank=True)),
                ('vat_number', models.CharField(max_length=20, verbose_name='VAT number', blank=True)),
                ('telephone', models.CharField(blank=True, help_text='format : +32475123456', max_length=20, verbose_name='Telephone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('start_time', models.TimeField(default=b'09:00', verbose_name='Start time')),
                ('end_time', models.TimeField(default=b'18:00', verbose_name='End time')),
                ('view_busy_slot', models.BooleanField(default=True, verbose_name='Can see busy slots')),
                ('view_in_list', models.BooleanField(default=True, verbose_name='Can see in doctors list')),
                ('confirm', models.TextField(null=True, verbose_name='Confirm key', blank=True)),
                ('text_rdv', models.TextField(null=True, verbose_name='Text RDV', blank=True)),
                ('text_horaires', models.TextField(null=True, verbose_name='Text horaires', blank=True)),
                ('timezone', timezone_field.fields.TimeZoneField(default=b'Europe/Brussels')),
                ('can_recharge', models.BooleanField(default=True, verbose_name='Can recharge type of subscription ')),
                ('address', address.models.AddressField(to='address.Address')),
                ('colorslots', models.ManyToManyField(to='doctor.ColorSlot', verbose_name='ColorSlot', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('date_start', models.DateField(verbose_name='Start date')),
                ('date_end', models.DateField(verbose_name='End date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('price_exVAT', models.FloatField(default=0.0, verbose_name='Price excl. VAT')),
                ('VAT', models.FloatField(default=21, verbose_name='VAT (%)')),
                ('price_VAT', models.FloatField(default=0.0, verbose_name='Price VAT', blank=True)),
                ('price_incVAT', models.FloatField(default=0.0, verbose_name='Price inc. VAT', blank=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('date_paid', models.DateField(null=True, verbose_name='date paid', blank=True)),
                ('note_paid', models.CharField(max_length=100, verbose_name='note paid', blank=True)),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('invoice_number', models.IntegerField(default=0, blank=True)),
                ('path', models.CharField(max_length=255, null=True, verbose_name='path', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=2015, verbose_name='Year')),
                ('number', models.IntegerField(default=0, verbose_name='Number')),
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
            field=models.ForeignKey(verbose_name='Type of subscription', to='doctor.TypePrice'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='invoices',
            field=models.ManyToManyField(to='doctor.Invoice', verbose_name='Invoices', blank=True),
        ),
    ]
