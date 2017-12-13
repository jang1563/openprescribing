# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-13 13:55
from __future__ import unicode_literals

from datetime import date
from django.db import migrations


def convert_to_dates(apps, schema_editor):
    NCSOConcession = apps.get_model('dmd', 'NCSOConcession')
    for concession in NCSOConcession.objects.all():
        year, month = concession.year_and_month.split('_')
        concession.date = date(int(year), int(month), 1)
        concession.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dmd', '0006_ncsoconcession_date'),
    ]

    operations = [
        migrations.RunPython(convert_to_dates),
    ]
