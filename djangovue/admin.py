from django.contrib import admin
from .models import Sensor, Metric, Unit, Measurement

# Register your models here

admin.site.register(Sensor)
admin.site.register(Metric)
admin.site.register(Unit)
admin.site.register(Measurement)
