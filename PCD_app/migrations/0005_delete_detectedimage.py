# Generated by Django 4.1.7 on 2023-05-15 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PCD_app", "0004_detectedimage_delete_nametester_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="DetectedImage",
        ),
    ]