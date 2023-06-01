# Generated by Django 3.1 on 2023-01-17 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20230117_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='tags',
            field=models.ManyToManyField(to='forum.Tags'),
        ),
        migrations.AlterField(
            model_name='forumcomment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 20, 52, 9, 582081)),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 17, 20, 52, 9, 580480)),
        ),
    ]
