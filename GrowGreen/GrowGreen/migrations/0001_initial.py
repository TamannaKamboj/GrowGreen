# Generated by Django 3.1 on 2021-10-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Pno', models.AutoField(primary_key=True, serialize=False)),
                ('Pname', models.CharField(max_length=50)),
                ('Pdiscription', models.TextField()),
                ('PContent', models.TextField()),
                ('PAuthor', models.CharField(max_length=50)),
            ],
        ),
    ]
