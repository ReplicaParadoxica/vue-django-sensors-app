from django.db import models


class SensorType(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    version = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255, default='Unnamed Sensor Type')


class Sensor(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True,
                            blank=True, default='Unnamed Sensor')
    type = models.ForeignKey(
        SensorType, on_delete=models.CASCADE, related_name='sensors')
    variant = models.PositiveIntegerField(
        null=True, blank=True, default=0)


class Metric(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='')


class Unit(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, default='Unnamed')
    precision = models.PositiveIntegerField(
        default=0)
    metric = models.ForeignKey(
        Metric, on_delete=models.CASCADE, related_name='units')
    selected = models.BooleanField(default=False)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    metric = models.ForeignKey(
        Metric, on_delete=models.CASCADE, related_name='measurements')
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, related_name='measurements')
    value = models.FloatField(null=True, blank=True, default=0)
