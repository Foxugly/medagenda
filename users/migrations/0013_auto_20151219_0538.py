# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_userprofile_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.CharField(default=1, max_length=8, verbose_name='language', choices=[(b'fr', 'Francais'), (b'nl', 'Nederlands'), (b'en', 'English')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='speciality',
            field=models.IntegerField(verbose_name='Speciality', choices=[(1, 'M\xe9decine G\xe9n\xe9rale'), (2, 'P\xe9diatrie'), (3, 'ORL'), (4, 'Cardiologue'), (5, 'Dentiste'), (13, 'Infirmier(\xe8re) ind\xe9pendant(e)'), (14, 'Kin\xe9sith\xe9rapeute'), (15, 'Ost\xe9opathe')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.IntegerField(verbose_name='Title', choices=[(1, 'Professeur'), (2, 'Docteur'), (3, 'Madame'), (4, 'Monsieur')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='view_busy_slot',
            field=models.BooleanField(default=True, verbose_name='Can see busy slots'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='view_in_list',
            field=models.BooleanField(default=True, verbose_name='Can see in doctors list'),
        ),
    ]
