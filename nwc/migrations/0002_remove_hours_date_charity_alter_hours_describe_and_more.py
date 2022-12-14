# Generated by Django 4.1.4 on 2022-12-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nwc", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="hours", name="date_charity",),
        migrations.AlterField(
            model_name="hours", name="describe", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="hours",
            name="hours_work",
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name="hours", name="name", field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="hours",
            name="service_work",
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name="hours", name="type_work", field=models.CharField(max_length=20),
        ),
    ]
