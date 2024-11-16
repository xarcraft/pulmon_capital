from rest_framework import serializers
from .models import CalidadAire

class CalidadAireSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalidadAire
        fields = ['sensor_id', 'ica', 'proximidad', 'fecha_hora']
