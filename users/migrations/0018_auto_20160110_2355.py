# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
        ('users', '0017_auto_20160107_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='type_price',
        ),
        migrations.DeleteModel(
            name='InvoiceNumber',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='can_recharge',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='colorslots',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='invoices',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slots',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='text_horaires',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='text_rdv',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='title',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='vat_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='view_busy_slot',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='view_in_list',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='weektemplate',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_doctor',
            field=models.ForeignKey(related_name='current_doctor', verbose_name='Doctor', to='doctor.Doctor', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='doctors',
            field=models.ManyToManyField(related_name='doctors', verbose_name='Doctors', to='doctor.Doctor', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(null=True, verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ColorSlot',
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
        migrations.DeleteModel(
            name='TypePrice',
        ),
    ]
