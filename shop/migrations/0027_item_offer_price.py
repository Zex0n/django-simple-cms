# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-30 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20180716_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='offer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой'),
        ),
    ]
