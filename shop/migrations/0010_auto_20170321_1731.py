# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 14:31
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170321_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.AddField(
            model_name='category',
            name='file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='category', verbose_name='Обложка для категории 250X250'),
        ),
        migrations.AddField(
            model_name='item',
            name='file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='category', verbose_name='Обложка для категории 250X250'),
        ),
    ]
