# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-10 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0010_auto_20220409_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_splitter',
            name='owes',
            field=models.IntegerField(blank=True),
        ),
    ]
