# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_choices',
            field=models.IntegerField(choices=[(0, 'deliver'), (1, 'normal')], default=0, verbose_name='AddressChoices'),
        ),
    ]