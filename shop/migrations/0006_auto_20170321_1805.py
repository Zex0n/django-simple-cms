# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170320_1449'),
    ]

    operations = [        
        
        
        migrations.AddField(
            model_name='item',
            name='offer_text',
            field=models.TextField(default='', verbose_name='Описание предложения'),
        ),
        
        
    ]
