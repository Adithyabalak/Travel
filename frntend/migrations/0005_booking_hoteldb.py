# Generated by Django 4.2.7 on 2024-03-27 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntend', '0004_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_hoteldb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peoples', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('hotel_name', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
