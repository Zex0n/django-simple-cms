# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='template',
            field=models.IntegerField(choices=[(0, 'menu.html')], default=0),
        ),
    ]
