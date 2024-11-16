from django.db import models

# Create your models here.
class CalidadAire(models.Model): 
    sensor_id = models.CharField(max_length=100) 
    ica = models.FloatField() 
    proximidad = models.FloatField() 
    fecha_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'calidad de aire'
        verbose_name_plural = 'Aire'
        ordering = ['ica']
