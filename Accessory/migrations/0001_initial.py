# Generated by Django 4.0.3 on 2022-04-11 11:23

import Accessory.models
import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(default='', max_length=100)),
                ('dayOfManufacture', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('insurance', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('thumbnail', models.ImageField(default=None, upload_to=Accessory.models.create_phoneThumbnail_directory)),
                ('description', tinymce.models.HTMLField()),
                ('price', models.IntegerField(default=0)),
                ('saleOff', models.FloatField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('sold', models.IntegerField(default=0)),
                ('keywordsSearch', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='AccessoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to=Accessory.models.create_phoneImage_directory)),
                ('accessory', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Accessory.accessory')),
            ],
        ),
    ]
