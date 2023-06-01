# Generated by Django 4.2.1 on 2023-05-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipment', '0006_delete_location_delete_locationimport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.IntegerField()),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LocationImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
