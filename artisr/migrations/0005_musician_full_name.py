# Generated by Django 4.2.1 on 2023-07-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artisr', '0004_remove_musician_tieu_su'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='full_name',
            field=models.TextField(null=True),
        ),
    ]
