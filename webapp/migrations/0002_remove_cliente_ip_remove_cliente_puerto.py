# Generated by Django 4.2.7 on 2023-11-23 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='puerto',
        ),
    ]
