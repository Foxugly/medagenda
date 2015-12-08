# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='confirm',
            field=models.TextField(null=True, verbose_name='Confirm key', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='end_time',
            field=models.TimeField(default=b'18:00', verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(max_length=2, verbose_name='language', choices=[(b'fr', 'Francais'), (b'nl', 'Nederlands'), (b'en', 'English')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slots',
            field=models.ManyToManyField(to='agenda.Slot', verbose_name='Slots', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(verbose_name='slug', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='speciality',
            field=models.IntegerField(verbose_name='Speciality', choices=[(1, 'Aucune'), (2, 'M\xe9decine G\xe9n\xe9rale'), (3, 'M\xe9decine Interne')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='start_time',
            field=models.TimeField(default=b'09:00', verbose_name='Start time'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=20, verbose_name='Telephone', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.IntegerField(default=2, verbose_name='Title', choices=[(1, 'Professeur'), (2, 'Docteur'), (3, 'Madame'), (4, 'Monsieur')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vat_number',
            field=models.CharField(max_length=20, verbose_name='VAT number', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='view_busy_slot',
            field=models.BooleanField(verbose_name='Can see busy slots'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='view_in_list',
            field=models.BooleanField(verbose_name='Can see in doctors list'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weektemplate',
            field=models.ForeignKey(verbose_name='Week template', blank=True, to='agenda.WeekTemplate', null=True),
        ),
    ]
