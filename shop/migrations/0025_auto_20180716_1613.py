# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-16 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20180716_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='new_flag_color',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Цвет подложки надписи'),
        ),
        migrations.AddField(
            model_name='category',
            name='new_flag_text',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Текст надписи НОВИНКА'),
        ),
    ]
