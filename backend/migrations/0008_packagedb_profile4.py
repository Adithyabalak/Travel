# Generated by Django 4.2.7 on 2024-03-06 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_country2_packagedb_country1'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagedb',
            name='profile4',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
