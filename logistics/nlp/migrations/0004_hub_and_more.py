# Generated by Django 4.1.7 on 2023-04-18 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0003_warehouseowner_warehouse_trucks'),
    ]

    operations = [
        migrations.CreateModel(
            name='hub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.CharField(max_length=6)),
                ('hub_storage_capacity', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='trucks',
            old_name='storage_capacity',
            new_name='truck_storage_capacity',
        ),
        migrations.RenameModel(
            old_name='WarehouseOwner',
            new_name='hubowner',
        ),
        migrations.DeleteModel(
            name='Warehouse',
        ),
        migrations.AddField(
            model_name='hub',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nlp.hubowner'),
        ),
    ]
