# Generated by Django 4.0.dev20210219192511 on 2021-03-09 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_rename_name_category_cat_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.category'),
        ),
    ]
