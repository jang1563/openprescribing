# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-19 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0037_auto_20181130_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='quantity_means_pack',
            field=models.NullBooleanField(default=None),
        ),
    ]
