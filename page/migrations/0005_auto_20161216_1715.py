# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20161213_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='placeholder',
            field=models.CharField(blank=True, help_text='Используйте в шаблоне тег {% placeholder horizontal_menu %}', max_length=255, verbose_name='Место для установки в шаблоне'),
        ),
        migrations.AlterField(
            model_name='page',
            name='application',
            field=models.CharField(blank=True, choices=[(0, 'Нет')], default='', max_length=255, verbose_name='Приложение'),
        ),
        migrations.AlterField(
            model_name='page',
            name='redirect_url',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='URL для редиректа'),
        ),
    ]
