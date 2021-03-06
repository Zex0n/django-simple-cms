# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 13:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0013_auto_20170619_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000, verbose_name='Ваше имя')),
                ('phone', models.CharField(default='', max_length=1000, verbose_name='Телефон')),
                ('company_name', models.CharField(default='', max_length=1000, verbose_name='Название компании')),
                ('inn', models.CharField(default='', max_length=1000, verbose_name='ИНН')),
                ('city', models.CharField(default='', max_length=1000, verbose_name='Город')),
                ('adres', models.CharField(default='', max_length=1000, verbose_name='Адрес доставки')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_name_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователя',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='min_offer',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Минимальная партия'),
        ),
    ]
