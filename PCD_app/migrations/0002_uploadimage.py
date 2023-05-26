# Generated by Django 4.1.7 on 2023-05-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PCD_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UploadImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
