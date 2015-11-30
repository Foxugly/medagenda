# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import address.models
from django.conf import settings
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=b'pic/profil.jpg', upload_to=b'pic')),
                ('speciality', models.CharField(max_length=10, choices=[(b'medgen', 'Medecine Generale'), (b'medint', 'Medecine Interne')])),
                ('slug', models.SlugField(blank=True)),
                ('language', models.CharField(max_length=2, choices=[(b'fr', 'Francais'), (b'nl', 'Nederlands'), (b'en', 'English')])),
                ('free_slot_color', colorfield.fields.ColorField(default=b'#00FF00', max_length=10)),
                ('busy_slot_color', colorfield.fields.ColorField(default=b'#FF0000', max_length=10)),
                ('address', address.models.AddressField(to='address.Address')),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
