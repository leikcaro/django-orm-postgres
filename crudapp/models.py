from django.db import models

# Create your models here.

class Empleado(models.Model):
    emp_id = models.CharField(max_length=3)
    emp_nombre = models.CharField(max_length=200)
    emp_correo = models.EmailField()
    emp_designacion = models.CharField(max_length=150)
    
def __str__(self):
    return self.emp_nombre