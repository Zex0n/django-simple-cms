# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 07:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20170202_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselslide',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Текст'),
        ),
    ]
