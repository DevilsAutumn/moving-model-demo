# Generated by Django 5.0.dev20230806144525 on 2023-08-08 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_eighteen", "0004_unrelatedmodel_remove_book_author"),
        ("test_seventeen", "0002_book_alter_unrelatedmodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookgenre",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="test_seventeen.book"
            ),
        ),
        migrations.AlterField(
            model_name="genre",
            name="m2m_field",
            field=models.ManyToManyField(to="test_seventeen.book"),
        ),
        migrations.AlterModelOptions(
            name="unrelatedmodel",
            options={},
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]