# Generated by Django 2.2.1 on 2019-05-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0120_auto_20190509_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email_known_to_work',
            field=models.BooleanField(default=False),
        ),
    ]
