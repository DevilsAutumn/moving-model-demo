# Generated by Django 5.0.dev20230806144525 on 2023-08-11 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_nineteen", "0003_alter_article_options"),
        ("test_twenty", "0003_alter_article_options_alter_reader_article"),
    ]

    operations = [
        migrations.DeleteModel(
            name="article",
        ),
    ]