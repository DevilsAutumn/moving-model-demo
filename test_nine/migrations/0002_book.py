# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_nine", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="book",
            fields=[
                ("id", models.UUIDField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_eight.author",
                    ),
                ),
            ],
            options={
                "db_table": "test_eight_book",
                "indexes": [],
                "constraints": [],
                "managed": False,
            },
        ),
    ]