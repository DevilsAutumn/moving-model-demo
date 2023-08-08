# Generated by Django 5.0.dev20230806144525 on 2023-08-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_eighteen", "0003_alter_book_options"),
        ("test_seventeen", "0002_book_bookgenre_alter_publisher_books_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookgenre",
            options={"managed": False},
        ),
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.AlterField(
            model_name="genre",
            name="m2m_field",
            field=models.ManyToManyField(to="test_seventeen.book"),
        ),
    ]