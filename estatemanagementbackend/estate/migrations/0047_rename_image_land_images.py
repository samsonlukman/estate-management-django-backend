# Generated by Django 5.0.2 on 2024-03-18 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0046_remove_building_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='image',
            new_name='images',
        ),
    ]