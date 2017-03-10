# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170309_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_variation',
            name='price_1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена 1'),
        ),
        migrations.AlterField(
            model_name='item_variation',
            name='price_2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена 2'),
        ),
        migrations.AlterField(
            model_name='item_variation',
            name='price_3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена 3'),
        ),
    ]
