# Generated by Django 4.2 on 2023-04-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0007_alter_trucks_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='trucks',
            name='location',
            field=models.CharField(default='hyd', max_length=100),
            preserve_default=False,
        ),
    ]
