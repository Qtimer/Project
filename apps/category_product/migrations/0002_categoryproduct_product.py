# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('category_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]