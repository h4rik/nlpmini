# Generated by Django 4.2 on 2023-04-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('aadhar', models.CharField(max_length=12)),
                ('license', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
