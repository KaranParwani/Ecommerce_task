# Generated by Django 4.0.dev20210219192511 on 2021-03-10 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_cart_cartproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='item',
            new_name='product',
        ),
    ]
