# Generated by Django 2.1.2 on 2018-11-06 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20181103_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeblock',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='timeblock',
            name='recorded_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
