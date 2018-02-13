# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_menu_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='application',
            field=models.CharField(choices=[(0, 'Нет')], default='', max_length=255, verbose_name='Приложение'),
        ),
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.IntegerField(choices=[(0, 'Страница'), (1, 'Ссылка'), (2, 'Приложение')], default=0, verbose_name='Тип страницы'),
        ),
        migrations.AddField(
            model_name='page',
            name='redirect_url',
            field=models.CharField(default='', max_length=1000, verbose_name='URL для редиректа'),
        ),
    ]
