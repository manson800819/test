# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-11 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20200310_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_t', to='shop.Type1'),
        ),
    ]
