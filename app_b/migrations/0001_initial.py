# Generated by Django 5.0.dev20230816142938 on 2023-08-16 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_a", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookGenre",
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
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app_a.book"
                    ),
                ),
                ("genre", models.ManyToManyField(to="app_a.publisher")),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=50)),
                ("m2m_field", models.ManyToManyField(to="app_a.book")),
            ],
        ),
    ]