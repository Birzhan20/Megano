# Generated by Django 4.2.7 on 2024-08-09 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_avatar_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Avatar",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
