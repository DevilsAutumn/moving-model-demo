# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_thirteen", "0002_book"),
        ("test_twelve", "0002_alter_book_options_alter_publisher_books_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={},
        ),
        migrations.AddField(
            model_name="genre",
            name="m2m_field",
            field=models.ManyToManyField(to="test_thirteen.book"),
        ),
        migrations.AlterField(
            model_name="bookgenre",
            name="book",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="test_thirteen.book"
            ),
        ),
    ]