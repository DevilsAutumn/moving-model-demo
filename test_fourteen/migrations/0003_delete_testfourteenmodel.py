# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_fifteen", "0003_alter_testfourteenmodel_options_and_more"),
        ("test_fourteen", "0002_alter_testfourteenmodel_options"),
    ]

    operations = [
        migrations.DeleteModel(
            name="testfourteenmodel",
        ),
    ]
