# Generated by Django 4.2.5 on 2023-10-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_user_followers_user_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followed_opps",
            field=models.ManyToManyField(blank=True, to="main.opportunity"),
        ),
    ]
