# Generated by Django 5.0.dev20230806144525 on 2023-08-08 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="mymodel",
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
                    "main_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_six.mainmodel",
                    ),
                ),
                (
                    "m2m_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_six.mymodelm2m",
                    ),
                ),
            ],
            options={
                "db_table": "test_six_mymodel",
                "indexes": [],
                "constraints": [],
                "managed": False,
            },
        ),
    ]
