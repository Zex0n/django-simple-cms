# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_category_new_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='new_flag',
            field=models.BooleanField(default=False, verbose_name='Показывать как новинку'),
        ),
    ]
