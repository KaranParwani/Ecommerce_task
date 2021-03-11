# Generated by Django 4.0.dev20210219192511 on 2021-03-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0022_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='order',
            name='ZipCode',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address1',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address2',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
