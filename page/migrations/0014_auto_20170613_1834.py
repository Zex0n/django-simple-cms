# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='fb_link',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ссылка на группу Фейсбук'),
        ),
        migrations.AddField(
            model_name='setting',
            name='vk_link',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ссылка на группу Вконтакте'),
        ),
    ]
