# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_address_address_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='primary',
            field=models.BooleanField(default=True, verbose_name='PrimaryAddress'),
        ),
    ]
