# Generated by Django 5.0.2 on 2024-02-27 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0014_country_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country',
        ),
    ]
