# Generated by Django 2.0.6 on 2018-06-08 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20180608_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='restaurante',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='valor',
        ),
    ]