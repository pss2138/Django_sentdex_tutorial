# Generated by Django 3.1 on 2020-08-25 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 9, 51, 33, 141044), verbose_name='date published'),
        ),
    ]
