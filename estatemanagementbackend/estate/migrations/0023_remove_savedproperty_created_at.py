# Generated by Django 5.0.2 on 2024-02-28 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0022_alter_building_country_alter_land_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedproperty',
            name='created_at',
        ),
    ]