# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-21 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0031_auto_20160816_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
