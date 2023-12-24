# Generated by Django 4.2.5 on 2023-10-27 05:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_user_followed_opps"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="forum",
            name="username",
        ),
        migrations.AddField(
            model_name="forum",
            name="user",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
