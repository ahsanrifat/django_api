# Generated by Django 4.0rc1 on 2021-12-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0005_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/%y'),
        ),
    ]
