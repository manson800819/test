# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-10 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200310_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Type1'),
        ),
    ]
