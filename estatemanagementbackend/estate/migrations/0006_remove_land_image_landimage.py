# Generated by Django 5.0.2 on 2024-02-26 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_land_image_delete_landimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='land',
            name='image',
        ),
        migrations.CreateModel(
            name='LandImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='property_images/')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_images', to='estate.land')),
            ],
        ),
    ]