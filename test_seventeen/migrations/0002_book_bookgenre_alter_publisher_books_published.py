# Generated by Django 5.0.dev20230806144525 on 2023-08-08 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_seventeen", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "test_eighteen_book",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="bookgenre",
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_seventeen.book",
                    ),
                ),
                ("genre", models.ManyToManyField(to="test_eighteen.genre")),
            ],
            options={
                "db_table": "test_eighteen_bookgenre",
                "indexes": [],
                "constraints": [],
                "managed": False,
            },
        ),
        migrations.AlterField(
            model_name="publisher",
            name="books_published",
            field=models.ManyToManyField(to="test_seventeen.book"),
        ),
    ]
