# Generated by Django 4.2.1 on 2023-06-03 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artisr', '0003_musician_tieu_su'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='tieu_su',
        ),
    ]
