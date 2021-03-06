# Generated by Django 3.1 on 2020-08-07 04:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
                ('sowing', models.TextField()),
                ('spacing', models.TextField()),
                ('harvest_min', models.IntegerField(default=1)),
                ('harvest_max', models.IntegerField(default=1)),
                ('companions', models.TextField(default='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PlantSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('date_seeded', models.DateField(blank=True, default=None, null=True)),
                ('date_planted', models.DateField(blank=True, null=True)),
                ('date_harvested', models.DateField(blank=True, default=None, null=True)),
                ('harvest_date_min', models.DateField(blank=True, null=True)),
                ('harvest_date_max', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.CharField(default=',,,,,,,,,,,', max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unnamed', max_length=100)),
                ('color', models.CharField(default='#C0BD7C', max_length=100)),
                ('location_description', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('zone', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('min_temp', models.IntegerField()),
            ],
        ),
    ]
