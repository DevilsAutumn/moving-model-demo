# Generated by Django 5.0.dev20230820143938 on 2023-08-21 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_eighteen", "0004_alter_bookgenre_options_alter_genre_m2m_field"),
        ("test_seventeen", "0002_book_bookgenre_alter_publisher_books_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bookgenre",
            options={},
        ),
    ]
