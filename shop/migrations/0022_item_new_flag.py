# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-09 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_item_min_lot'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='new_flag',
            field=models.BooleanField(default=False, verbose_name='Показывать как новинку'),
        ),
    ]
