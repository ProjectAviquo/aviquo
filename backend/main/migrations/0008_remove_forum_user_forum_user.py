# Generated by Django 4.2.5 on 2023-10-27 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_forum_username_forum_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='user',
        ),
        migrations.AddField(
            model_name='forum',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
