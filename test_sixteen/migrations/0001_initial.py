# Generated by Django 5.0.dev20230730140916 on 2023-08-01 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("test_fifteen", "0001_initial"),
        ("test_fourteen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestSixteenModel",
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
                ("some_data", models.CharField(max_length=50)),
                (
                    "test_fifteen_model",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_fifteen.testfifteenmodel",
                    ),
                ),
                (
                    "test_fourteen_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_fourteen.testfourteenmodel",
                    ),
                ),
            ],
        ),
    ]
