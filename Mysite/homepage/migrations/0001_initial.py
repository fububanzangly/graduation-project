# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-08 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(default='/', max_length=200, verbose_name='\u5e8f\u53f7')),
                ('path', models.CharField(default='/', max_length=200, verbose_name='\u8def\u5f84')),
            ],
        ),
    ]
