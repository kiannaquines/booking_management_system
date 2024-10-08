# Generated by Django 5.0.7 on 2024-09-27 03:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('truck_id', models.AutoField(primary_key=True, serialize=False)),
                ('truck_name', models.CharField(max_length=200)),
                ('truck_plate_number', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('truck_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Truck',
                'db_table': 'truck',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_date', models.DateField()),
                ('product_type', models.CharField(max_length=200)),
                ('load_count', models.IntegerField()),
                ('reservation_status', models.CharField(choices=[('Delivered', 'Delivered'), ('In Transit', 'In Transit'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('destination_longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('destination_latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('booking_client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('truck_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.truck')),
            ],
            options={
                'verbose_name': 'Booking',
                'db_table': 'bookings',
            },
        ),
    ]
