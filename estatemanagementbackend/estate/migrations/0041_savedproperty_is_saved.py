# Generated by Django 5.0.2 on 2024-03-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0040_alter_savedproperty_unique_together_savedland'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedproperty',
            name='is_saved',
            field=models.BooleanField(default=False),
        ),
    ]
