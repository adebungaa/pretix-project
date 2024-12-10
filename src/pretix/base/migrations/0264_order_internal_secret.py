# Generated by Django 4.2.11 on 2024-05-16 11:07

from django.db import migrations, models

import pretix.base.models.orders


class Migration(migrations.Migration):

    dependencies = [
        ("pretixbase", "0263_auto_20240409_0732"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="internal_secret",
            field=models.CharField(
                default=None,
                max_length=32,
                null=True,
            ),
        ),
    ]
