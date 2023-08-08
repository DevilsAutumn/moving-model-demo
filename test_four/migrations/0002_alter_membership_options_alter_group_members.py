# Generated by Django 5.0.dev20230806144525 on 2023-08-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_five", "0002_membership"),
        ("test_four", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="membership",
            options={"managed": False},
        ),
        migrations.AlterField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(
                through="test_five.Membership", to="test_four.person"
            ),
        ),
    ]
