# Generated by Django 4.2.7 on 2024-08-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="code",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="payment",
            name="month",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="payment",
            name="number",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="payment",
            name="year",
            field=models.IntegerField(),
        ),
    ]
