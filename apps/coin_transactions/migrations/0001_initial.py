# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-04 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_product_promote'),
        ('accounts', '0002_auto_20180304_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(0, 'Deposit'), (1, 'Withdraw'), (2, 'Usage')], verbose_name='Transaction Type')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Account', verbose_name='Transaction Owner')),
                ('promoted_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]