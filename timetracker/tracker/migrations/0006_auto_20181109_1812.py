# Generated by Django 2.1.2 on 2018-11-10 00:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20181109_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeblock',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
