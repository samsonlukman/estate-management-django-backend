# Generated by Django 5.0.2 on 2024-03-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0041_savedproperty_is_saved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedproperty',
            name='is_saved',
        ),
        migrations.AddField(
            model_name='building',
            name='is_saved',
            field=models.BooleanField(default=False),
        ),
    ]