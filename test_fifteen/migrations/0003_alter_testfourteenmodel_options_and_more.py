# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_fifteen", "0002_testfourteenmodel"),
        ("test_fourteen", "0002_alter_testfourteenmodel_options"),
        ("test_sixteen", "0002_rename_testsixteenmodel_newtestsixteenmodel_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="testfourteenmodel",
            options={},
        ),
        migrations.AddField(
            model_name="testfifteenmodel",
            name="f_m2m",
            field=models.ManyToManyField(
                related_name="fourteen_model_m2m",
                through="test_sixteen.NewTestSixteenModel",
                to="test_fifteen.testfourteenmodel",
            ),
        ),
        migrations.AddField(
            model_name="testfifteenmodel",
            name="test_fourteen_model",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fourteen_model",
                to="test_fifteen.testfourteenmodel",
            ),
            preserve_default=False,
        ),
    ]
