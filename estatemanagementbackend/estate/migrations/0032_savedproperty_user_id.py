# Generated by Django 5.0.2 on 2024-03-01 04:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0031_remove_savedproperty_property_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedproperty',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saved_properties_user', to=settings.AUTH_USER_MODEL),
        ),
    ]