# Generated by Django 4.2.1 on 2023-06-01 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0009_alter_location_options_alter_truck_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='zip_pickup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipment.location'),
        ),
    ]
