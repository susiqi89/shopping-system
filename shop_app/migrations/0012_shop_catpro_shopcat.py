# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-18 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0011_auto_20170818_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_catpro',
            name='shopcat',
            field=models.ManyToManyField(to='shop_app.shop_cat'),
        ),
    ]
