# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thex', '0003_auto_20170131_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transient',
            name='peak_brightness',
            field=models.FloatField(default=0.0),
        ),
    ]
