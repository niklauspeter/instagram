# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0006_auto_20190522_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile_photo',
        ),
    ]
