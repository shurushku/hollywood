# Generated by Django 4.1.3 on 2022-11-09 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_studio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="rating",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ]
            ),
        ),
    ]
