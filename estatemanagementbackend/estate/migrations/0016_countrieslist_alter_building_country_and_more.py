# Generated by Django 5.0.2 on 2024-02-27 14:32

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0015_remove_country_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='building',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.countrieslist'),
        ),
        migrations.AlterField(
            model_name='land',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.countrieslist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='estate.countrieslist'),
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]
