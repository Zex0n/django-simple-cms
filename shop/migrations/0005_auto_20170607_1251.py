# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-07 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_item_content_mall'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='content_mall',
            new_name='content_small',
        ),
    ]
