# Generated by Django 5.0.dev20230811145154 on 2023-08-11 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_twentyone", "0002_alter_book_options_alter_author_book_m2m"),
        ("test_twentytwo", "0002_book"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={},
        ),
        migrations.AlterField(
            model_name="product",
            name="book_fk",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="test_twentytwo.book"
            ),
        ),
    ]