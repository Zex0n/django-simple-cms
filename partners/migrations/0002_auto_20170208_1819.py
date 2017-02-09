# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 15:19
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealers',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Показывать'),
        ),
        migrations.AlterField(
            model_name='dealers',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]
