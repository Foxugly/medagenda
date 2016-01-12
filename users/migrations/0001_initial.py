# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(default=1, max_length=8, verbose_name='language', choices=[(b'fr', 'Francais'), (b'nl', 'Nederlands'), (b'en', 'English')])),
                ('confirm', models.TextField(null=True, verbose_name='Confirm key', blank=True)),
                ('accept', models.BooleanField(default=False, verbose_name='I accept the terms and conditions of use of Medagenda (see <a href="/conditions/"> here </a>)')),
                ('current_doctor', models.ForeignKey(related_name='current_doctor', verbose_name='Current doctor', to='doctor.Doctor', null=True)),
                ('doctors', models.ManyToManyField(related_name='doctors', verbose_name='Doctors', to='doctor.Doctor', blank=True)),
                ('user', models.OneToOneField(null=True, verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
