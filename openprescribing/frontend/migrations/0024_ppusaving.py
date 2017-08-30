# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-14 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0023_presentation_is_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPUSaving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('lowest_decile', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('price_per_unit', models.FloatField()),
                ('possible_savings', models.FloatField()),
                ('formulation_swap', models.TextField(blank=True, null=True)),
                ('pct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.PCT')),
                ('practice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.Practice')),
                ('presentation', models.ForeignKey(db_column=b'bnf_code', on_delete=django.db.models.deletion.CASCADE, to='frontend.Presentation')),
            ],
        ),
    ]