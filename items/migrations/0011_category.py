# Generated by Django 4.0.dev20210219192511 on 2021-03-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
