# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_five", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="membership",
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
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_four.person",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_four.group",
                    ),
                ),
                ("date_joined", models.DateField()),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "test_four_membership",
                "indexes": [],
                "constraints": [],
                "managed": False,
            },
        ),
    ]
