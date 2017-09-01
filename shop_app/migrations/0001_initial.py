# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-13 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, null=True, verbose_name='密码')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='邮箱')),
            ],
            options={
                'verbose_name_plural': '管理员表',
                'verbose_name': '管理员表',
                'ordering': ['-id'],
            },
        ),
    ]