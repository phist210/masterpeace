# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0015_remove_userprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.TextField(default='none', max_length=10000000000),
        ),
    ]