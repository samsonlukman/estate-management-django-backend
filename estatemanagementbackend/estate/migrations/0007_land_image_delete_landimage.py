# Generated by Django 5.0.2 on 2024-02-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_remove_land_image_landimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='property_images/'),
        ),
        migrations.DeleteModel(
            name='LandImage',
        ),
    ]
