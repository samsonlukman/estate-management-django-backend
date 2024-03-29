# Generated by Django 5.0.2 on 2024-03-01 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0030_alter_savedproperty_property_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedproperty',
            name='property',
        ),
        migrations.RemoveField(
            model_name='savedproperty',
            name='user',
        ),
        migrations.AddField(
            model_name='savedproperty',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties_image', to='estate.building'),
        ),
        migrations.AddField(
            model_name='savedproperty',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties_name', to='estate.building'),
        ),
        migrations.AddField(
            model_name='savedproperty',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties_price', to='estate.building'),
        ),
        migrations.AddField(
            model_name='savedproperty',
            name='property_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties_owner', to='estate.building'),
        ),
    ]
