# Generated by Django 4.0.dev20210219192511 on 2021-03-09 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_items_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='name',
        ),
    ]
