# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-18 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_shop_catpro_shopcat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop_catpro',
            name='shopcat',
        ),
        migrations.AddField(
            model_name='shop_cat',
            name='shopcat',
            field=models.ManyToManyField(to='shop_app.shop_catpro'),
        ),
    ]
