# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='待办内容')),
                ('is_done', models.BooleanField(default=False, verbose_name='事项状态')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '待办事项',
                'verbose_name_plural': '待办事项',
            },
        ),
    ]
