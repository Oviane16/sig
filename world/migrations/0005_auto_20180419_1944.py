# Generated by Django 2.0 on 2018-04-19 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20180419_1712'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorldBorder',
            new_name='Region',
        ),
    ]