# Generated by Django 4.0.dev20210219192511 on 2021-03-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.category'),
        ),
    ]
