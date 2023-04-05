from rest_framework import serializers
from .models import Sensor, Metric, Unit, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'type', 'variant']


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'name']


class UnitSerializer(serializers.ModelSerializer):
    metric_name = serializers.CharField(source='metric.name')

    class Meta:
        model = Unit
        fields = ['id', 'name', 'precision', 'metric_name', 'selected']


class MeasurementSerializer(serializers.ModelSerializer):
    sensor_name = serializers.CharField(source='sensor.name')
    metric_name = serializers.CharField(source='metric.name')
    unit_name = serializers.CharField(source='unit.name')
    unit_precision = serializers.IntegerField(source='unit.precision')

    class Meta:
        model = Measurement
        fields = ['sensor_name', 'metric_name', 'unit_name',
                  'unit_precision', 'value']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'type', 'variant', 'measurements']
