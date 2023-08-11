# Generated by Django 5.0.dev20230806144525 on 2023-08-11 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("test_nineteen", "0001_initial"),
        ("test_twenty", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="test_twenty.author"
            ),
        ),
    ]
