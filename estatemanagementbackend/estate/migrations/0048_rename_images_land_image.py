# Generated by Django 5.0.2 on 2024-03-18 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0047_rename_image_land_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='land',
            old_name='images',
            new_name='image',
        ),
    ]