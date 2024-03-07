# Generated by Django 4.2.7 on 2023-11-13 23:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("grass", "0002_remove_organization_created_by_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mapset",
            name="users",
            field=models.ManyToManyField(
                related_name="mapsets", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]