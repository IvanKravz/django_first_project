# Generated by Django 4.2.1 on 2023-05-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(max_length=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.DateField(max_length=10),
        ),
    ]
