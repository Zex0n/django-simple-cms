# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20170712_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='', max_length=1000, verbose_name='Контактное лицо'),
        ),
    ]
