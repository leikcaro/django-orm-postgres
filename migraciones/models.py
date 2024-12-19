from django.db import models
from datetime import datetime
# Create your models here.

class PrecioHistoricoVehiculos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    modelo = models.CharField(max_length=120)
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=10)


annos_choices = []
for r in range(1950, (datetime.now().year+2)): #mostrar en clases
    annos_choices.append((r,r))
def anno_actual():
    return datetime.date.today().year
class Automotriz(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
class ModeloCarro(models.Model):
    nombre = models.CharField(max_length=255)
    automotriz = models.ForeignKey(Automotriz, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=annos_choices, default=anno_actual)
    costo_fabricacion = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    precio_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.nombre