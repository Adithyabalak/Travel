# Generated by Django 4.2.7 on 2024-04-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frntend', '0008_delete_checkoutdb_remove_contactdb_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.IntegerField(blank=True, null=True)),
                ('monthyear', models.DateField(blank=True, null=True)),
                ('cvv', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
