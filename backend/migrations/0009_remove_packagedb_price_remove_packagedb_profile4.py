# Generated by Django 4.2.7 on 2024-03-06 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_packagedb_profile4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packagedb',
            name='price',
        ),
        migrations.RemoveField(
            model_name='packagedb',
            name='profile4',
        ),
    ]
