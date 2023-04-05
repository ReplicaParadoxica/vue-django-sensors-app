from django.urls import path
from .views import SensorListAPIView, MetricListAPIView, UnitListAPIView, MeasurementListAPIView, SensorDataAPIView

urlpatterns = [
    path('sensors/', SensorListAPIView.as_view(), name='sensor-list'),
    path('metrics/', MetricListAPIView.as_view(), name='metric-list'),
    path('units/', UnitListAPIView.as_view(), name='unit-list'),
    path('measurements/', MeasurementListAPIView.as_view(), name='measurement-list'),
    path('sensors/<int:sensor_id>/',
         SensorDataAPIView.as_view(), name='sensor-data'),
]
