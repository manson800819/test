# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-11 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20200311_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_t', to='shop.Type1'),
        ),
    ]
