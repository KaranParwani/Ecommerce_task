# Generated by Django 4.0.dev20210219192511 on 2021-03-09 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_items_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='category',
        ),
    ]