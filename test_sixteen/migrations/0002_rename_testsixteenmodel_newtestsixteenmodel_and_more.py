# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_fifteen", "0002_testfourteenmodel"),
        ("test_sixteen", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="TestSixteenModel",
            new_name="NewTestSixteenModel",
        ),
        migrations.AlterField(
            model_name="newtestsixteenmodel",
            name="test_fourteen_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="test_fifteen.testfourteenmodel",
            ),
        ),
    ]
