# Generated by Django 4.2.5 on 2023-10-01 17:44

from django.db import migrations, models

import apps.core.validators


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="chess_profile_url",
            field=models.URLField(
                blank=True,
                max_length=60,
                null=True,
                validators=[apps.core.validators.validate_chess_profile_url],
            ),
        ),
    ]
