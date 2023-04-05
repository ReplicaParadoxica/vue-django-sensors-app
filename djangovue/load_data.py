import json
from django.core.exceptions import ObjectDoesNotExist
from .models import SensorType, Sensor, Metric, Unit, Measurement


def load_sensor_types():
    with open('sensorTypes.json', 'r') as f:
        data = json.load(f)
        for type_id, versions in data.items():
            for version, type_data in versions.items():
                sensor_type = SensorType(id=int(type_id), version=int(
                    version), name=type_data['name'])
                sensor_type.save()


def load_metrics():
    with open('metrics.json', 'r') as f:
        data = json.load(f)
        for item in data['data']['items']:
            metric = Metric(id=int(item['id']), name=item['name'])
            metric.save()
            for unit_data in item['units']:
                unit = Unit(id=int(unit_data['id']), name=unit_data['name'],
                            precision=int(unit_data['precision']), selected=unit_data.get('selected', False))
                unit.metric = metric
                unit.save()


def load_sensors():
    with open('sensors.json', 'r') as f:
        data = json.load(f)
        for sensor_id, sensor_data in data.items():
            try:
                sensor_type = SensorType.objects.get(
                    id=sensor_data['type'], version=sensor_data['variant'])
            except ObjectDoesNotExist:
                continue

            sensor_name = sensor_data.get(
                'name', '').strip() or 'Unnamed Sensor'
            if not sensor_name:
                sensor_name = 'Unnamed Sensor'

            sensor = Sensor(id=int(sensor_id),
                            name=sensor_name, type=sensor_type)
            sensor.save()

            for metric_id, metric_data in sensor_data['metrics'].items():
                try:
                    metric = Metric.objects.get(id=int(metric_id))
                    unit = metric.units.get(selected=True)
                except ObjectDoesNotExist:
                    continue
                measurement = Measurement(
                    sensor=sensor, metric=metric, unit=unit, value=metric_data['v'])
                measurement.save()
