# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-26 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0015_auto_20180526_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='add_operation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='添加操作'),
        ),
        migrations.AddField(
            model_name='history',
            name='tixian_operation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='添加操作'),
        ),
        migrations.AddField(
            model_name='history',
            name='update_operation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='添加操作'),
        ),
    ]