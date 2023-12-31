# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-23 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('cost_of', models.IntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('discount', models.IntegerField(default=0, max_length=2, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430 (0 - \u0431\u0435\u0437 \u0441\u043a\u0438\u0434\u043a\u0438)')),
                ('main_photo', models.ImageField(upload_to=main.models.get_file_path, verbose_name='\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u0444\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u0430 \u0442\u043e\u0432\u0430\u0440\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.get_file_path, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Items')),
            ],
        ),
    ]
