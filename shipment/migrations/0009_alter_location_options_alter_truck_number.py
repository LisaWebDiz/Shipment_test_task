# Generated by Django 4.2.1 on 2023-05-28 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0008_truck_cargo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['zip']},
        ),
        migrations.AlterField(
            model_name='truck',
            name='number',
            field=models.CharField(max_length=5),
        ),
    ]
