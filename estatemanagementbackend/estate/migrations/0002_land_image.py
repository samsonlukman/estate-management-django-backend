# Generated by Django 5.0.2 on 2024-02-25 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='property_images/'),
        ),
    ]
