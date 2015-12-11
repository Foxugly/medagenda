# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20151210_0203'),
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
        migrations.RemoveField(
            model_name='userprofile',
            name='free_price_booked_slot_color',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='free_price_free_slot_color',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nhs_price_booked_slot_color',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nhs_price_free_slot_color',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='text_horaires',
            field=models.TextField(null=True, verbose_name='Text horaires', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='text_rdv',
            field=models.TextField(null=True, verbose_name='Text RDV', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='colorslots',
            field=models.ManyToManyField(to='users.ColorSlot', verbose_name='ColorSlot', blank=True),
        ),
    ]
