from django.contrib import admin
from .models import CalidadAire

# Register your models here.
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'ica', 'proximidad', 'fecha_hora')

admin.site.register(CalidadAire, MonitorAdmin)