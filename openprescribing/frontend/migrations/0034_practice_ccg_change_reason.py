# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-08 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0033_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='ccg_change_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]