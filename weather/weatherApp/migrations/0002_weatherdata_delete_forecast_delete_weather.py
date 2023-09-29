# Generated by Django 4.1.7 on 2023-09-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conditions', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Forecast',
        ),
        migrations.DeleteModel(
            name='Weather',
        ),
    ]
