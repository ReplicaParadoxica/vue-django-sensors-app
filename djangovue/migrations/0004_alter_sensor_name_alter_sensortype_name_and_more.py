# Generated by Django 4.2 on 2023-04-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangovue', '0003_sensortype_alter_measurement_value_alter_metric_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, default='Unnamed Sensor', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sensortype',
            name='name',
            field=models.CharField(default='Unnamed Sensor Type', max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(default='Unnamed', max_length=255),
        ),
    ]
