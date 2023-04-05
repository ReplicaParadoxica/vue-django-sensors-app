from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Metric, Unit, Measurement
from .serializers import SensorSerializer, MetricSerializer, UnitSerializer, MeasurementSerializer


class SensorListAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['type']
    ordering_fields = ['name']
    search_fields = ['name']


class MetricListAPIView(ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class UnitListAPIView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class MeasurementListAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['sensor__name', 'metric__name']
    ordering_fields = ['sensor__name', 'metric__name']
    search_fields = ['sensor__name']


class SensorDataAPIView(APIView):
    def get(self, request, sensor_id):
        sensor = Sensor.objects.get(id=sensor_id)
        data = {
            'name': sensor.name,
            'metrics': {},
        }
        for measurement in sensor.measurements.all():
            metric_name = measurement.metric.name
            unit_name = measurement.unit.name
            unit_precision = measurement.unit.precision
            value = measurement.value
            if value is None:
                continue
            if metric_name not in data['metrics']:
                data['metrics'][metric_name] = {
                    'unit': f"{metric_name} ({unit_name})",
                    'values': [],
                }
            data['metrics'][metric_name]['values'].append({'value': round(value, unit_precision),
                                                           })
        return Response(data)
