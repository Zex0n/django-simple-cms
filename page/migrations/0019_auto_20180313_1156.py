# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-13 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_banners'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='link_1_file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='links', verbose_name='Картинка первой ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_1_link',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='URL первой ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_1_text',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Текст первой ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_1_title',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Название первой ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_2_file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='links', verbose_name='Картинка второй ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_2_link',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='URL второй ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_2_text',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Текст второй ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_2_title',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Название второй ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_3_file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='links', verbose_name='Картинка третьей ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_3_link',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='URL третьей ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_3_text',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Текст третьей ссылки'),
        ),
        migrations.AddField(
            model_name='setting',
            name='link_3_title',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Название третьей ссылки'),
        ),
        migrations.AlterField(
            model_name='banners',
            name='banner_image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='banners', verbose_name='Картинка для баннера 270px X 120 px'),
        ),
    ]
