# Generated by Django 5.0.2 on 2024-02-28 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0023_remove_savedproperty_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='description',
            field=models.TextField(default='no description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='land',
            name='image',
            field=models.ImageField(default='no', upload_to='property_images/'),
            preserve_default=False,
        ),
    ]
