# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-06 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_app', '0017_auto_20170505_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemp',
            name='image',
            field=models.TextField(blank=True, max_length=10000000, null=True),
        ),
        migrations.AlterField(
            model_name='textmp',
            name='text',
            field=models.TextField(blank=True, max_length=10000000, null=True),
        ),
    ]
