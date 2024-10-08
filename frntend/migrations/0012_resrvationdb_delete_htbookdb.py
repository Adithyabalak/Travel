# Generated by Django 4.2.7 on 2024-07-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntend', '0011_rename_hotelbookdb_htbookdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='resrvationdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=100, null=True)),
                ('ch_out', models.DateField(blank=True, max_length=100, null=True)),
                ('gust', models.IntegerField(blank=True, null=True)),
                ('l_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mail', models.CharField(blank=True, max_length=100, null=True)),
                ('ch_in', models.IntegerField(blank=True, null=True)),
                ('types', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='htbookdb',
        ),
    ]
