# Generated by Django 5.0.1 on 2024-04-29 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_rename_movie_movie_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie_Details',
        ),
    ]