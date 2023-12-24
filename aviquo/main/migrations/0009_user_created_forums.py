# Generated by Django 4.2.5 on 2023-10-29 04:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_remove_forum_user_forum_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="created_forums",
            field=models.ManyToManyField(
                blank=True, related_name="creator", to="main.forum"
            ),
        ),
    ]
