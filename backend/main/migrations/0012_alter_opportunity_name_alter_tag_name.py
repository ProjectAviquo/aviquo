# Generated by Django 4.2.5 on 2023-12-23 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_opportunity_profile_image_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='name',
            field=models.CharField(help_text='Opportunity name/title', max_length=200, verbose_name='Opportunity'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Example: scholarship, extracurricular activity, etc.', max_length=50, unique=True, verbose_name='Tag'),
        ),
    ]