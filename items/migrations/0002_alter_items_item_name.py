# Generated by Django 4.0.dev20210219192511 on 2021-03-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]