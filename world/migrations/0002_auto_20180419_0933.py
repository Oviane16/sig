# Generated by Django 2.0 on 2018-04-19 06:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborder',
            name='area',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='fips',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='iso2',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='iso3',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='mpoly',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='pop2005',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='region',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='worldborder',
            name='un',
        ),
        migrations.AddField(
            model_name='worldborder',
            name='mpoint',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='name',
            field=models.CharField(default='Unknown location', max_length=50),
        ),
    ]