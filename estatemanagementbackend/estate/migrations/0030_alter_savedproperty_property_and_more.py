# Generated by Django 5.0.2 on 2024-02-29 22:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0029_alter_savedproperty_property_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedproperty',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.building'),
        ),
        migrations.AlterField(
            model_name='savedproperty',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
