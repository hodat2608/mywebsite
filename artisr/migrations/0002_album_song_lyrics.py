# Generated by Django 4.2.1 on 2023-06-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='song_lyrics',
            field=models.CharField(default='', max_length=1000000000),
        ),
    ]
