# Generated by Django 4.1.1 on 2022-09-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="building",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="room",
            name="location",
            field=models.CharField(default="", max_length=200),
        ),
    ]