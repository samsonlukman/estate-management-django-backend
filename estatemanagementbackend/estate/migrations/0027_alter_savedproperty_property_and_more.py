# Generated by Django 5.0.2 on 2024-02-29 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0026_remove_savedproperty_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedproperty',
            name='property',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='savedproperty',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
