from django.shortcuts import render
from rest_framework import generics
from .models import CalidadAire
from .serializers import CalidadAireSerializer

# Create your views here.
class CalidadAireList(generics.ListCreateAPIView):
    queryset = CalidadAire.objects.all()
    serializer_class = CalidadAireSerializer

class CalidadAireDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalidadAire.objects.all()
    serializer_class = CalidadAireSerializer


def obtener_datos_sensor(sensor_id):
    datos = {
        'sensor_id': sensor_id,
        'ica': 50,  # Ejemplo de valor de ICA
        'proximidad': 10,  # Ejemplo de valor de proximidad
    }
    return datos

def insertar_datos(datos):
    calidadaire = CalidadAire.objects.create(**datos)
    calidadaire.save()


def vista_calidad_aire(request):
    datos = CalidadAire.objects.all()
    print(datos)
    return render(request, 'monitor/index.html', {'datos': datos})


""" 
INDICE DE CALIDAD DEL AIRE - ICA (Indice de Calidad del Aire)
CONCENTRACION DE NO2(DIOXIDO DE NITROGENO) DE LA ULTIMA HORA
0-40 BUENA
41-90 RAZONABLEMENTE BUENA
91-120 REGULAR
121-230 DESFAVORABLE
231-340 MUY DESFAVORABLE
341-1000 EXTREMADAMENTE DESFAVORABLE
"""