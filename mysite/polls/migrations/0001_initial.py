# Generated by Django 3.2.5 on 2022-10-20 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=200, null=True)),
                ('rider_phone', models.CharField(max_length=200, null=True)),
                ('from_location', models.CharField(max_length=200)),
                ('to_location', models.CharField(max_length=200)),
                ('travel_medium', models.IntegerField(default=0)),
                ('travel_datetime', models.DateTimeField(verbose_name='travel date time')),
                ('flexible_timing', models.BooleanField(default=False)),
                ('no_of_assets', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=200)),
                ('from_location', models.CharField(max_length=200)),
                ('to_location', models.CharField(max_length=200)),
                ('flexible_timing', models.BooleanField(default=False)),
                ('travel_datetime', models.DateTimeField(verbose_name='travel date time')),
                ('no_of_assets', models.IntegerField(default=0)),
                ('asset_type', models.IntegerField(default=0)),
                ('asset_sentivity', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('delivery_info', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('assigned_rider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riders', to='polls.riders')),
            ],
        ),
    ]
