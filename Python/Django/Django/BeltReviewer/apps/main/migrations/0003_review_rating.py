# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180221_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=5, max_length=1),
            preserve_default=False,
        ),
    ]
