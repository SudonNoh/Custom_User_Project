# Generated by Django 3.2.8 on 2021-10-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_image_profile_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fllows',
            field=models.ManyToManyField(related_name='followed_by', to='profiles.Profile'),
        ),
    ]