# Generated by Django 4.1.3 on 2022-11-17 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20220112_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 17, 17, 53, 56, 413581)),
        ),
    ]
