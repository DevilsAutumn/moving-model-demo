# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "test_one",
            "0002_alter_mymodel_options_alter_myrelatedmodels_field_fk_and_more",
        ),
        ("test_two", "0002_mymodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mymodel",
            options={},
        ),
        migrations.AlterField(
            model_name="myothermodel",
            name="field_fk",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="test_two.mymodel",
            ),
        ),
    ]
