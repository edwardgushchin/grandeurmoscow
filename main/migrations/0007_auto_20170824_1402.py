# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-24 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170824_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='category',
        ),
        migrations.RemoveField(
            model_name='items',
            name='room',
        ),
    ]