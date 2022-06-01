# Generated by Django 4.0.3 on 2022-06-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_order_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='order',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='reciverName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
