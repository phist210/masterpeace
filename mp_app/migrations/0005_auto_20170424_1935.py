# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0004_auto_20170424_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/user_images/'),
        ),
    ]
