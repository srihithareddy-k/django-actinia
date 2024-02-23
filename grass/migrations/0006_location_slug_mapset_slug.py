# Generated by Django 4.2.7 on 2024-01-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grass", "0005_region_rename_users_location_actinia_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="slug",
            field=models.SlugField(
                blank=True, editable=False, max_length=150, unique=True
            ),
        ),
        migrations.AddField(
            model_name="mapset",
            name="slug",
            field=models.SlugField(
                blank=True, editable=False, max_length=150, unique=True
            ),
        ),
    ]
