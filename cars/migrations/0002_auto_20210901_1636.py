# Generated by Django 3.2.7 on 2021-09-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_id',
            new_name='purchaser',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.IntegerField(default=0),
        ),
    ]