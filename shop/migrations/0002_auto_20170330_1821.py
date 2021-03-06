# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='offer_name1',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Наименование бренд'),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer_name2',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Наименование модель'),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer_text1',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Строка описания 1:'),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer_text2',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Строка описания 2:'),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer_text_cost',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer_text_price',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Цена текст'),
        ),
    ]
