# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
        ('users', '0003_auto_20151130_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='busy_slot_color',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='free_slot_color',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='free_price_booked_slot_color',
            field=colorfield.fields.ColorField(default=b'#F64636', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='free_price_free_slot_color',
            field=colorfield.fields.ColorField(default=b'#73B5EB', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nhs_price_booked_slot_color',
            field=colorfield.fields.ColorField(default=b'#F64636', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nhs_price_free_slot_color',
            field=colorfield.fields.ColorField(default=b'#73EB79', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slots',
            field=models.ManyToManyField(to='agenda.Slot', verbose_name='slots', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='title',
            field=models.IntegerField(default=2, choices=[(1, 'Professeur'), (2, 'Docteur'), (3, 'Madame'), (4, 'Monsieur')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='view_in_list',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weektemplate',
            field=models.ForeignKey(blank=True, to='agenda.WeekTemplate', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='speciality',
            field=models.IntegerField(choices=[(1, 'Aucune'), (2, 'M\xe9decine G\xe9n\xe9rale'), (3, 'M\xe9decine Interne')]),
        ),
    ]
