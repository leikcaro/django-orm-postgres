from django.db import models

from django.db import models

class Operacion(models.Model):
    """
    Modelo que representa una operación aritmética.
    Permite 4 tipos: Suma, Resta, Multiplicación y División.
    """
    TIPO_OPERACION = (
        ('S', 'Suma'),
        ('R', 'Resta'),
        ('M', 'Multiplicación'),
        ('D', 'División'),
    )

    tipo = models.CharField(max_length=1, choices=TIPO_OPERACION)
    valor1 = models.DecimalField(max_digits=10, decimal_places=2)
    valor2 = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def calcular_resultado(self):
        if self.tipo == 'S':
            return self.valor1 + self.valor2
        elif self.tipo == 'R':
            return self.valor1 - self.valor2
        elif self.tipo == 'M':
            return self.valor1 * self.valor2
        elif self.tipo == 'D':
            if self.valor2 == 0:
                # Lanzamos un error si se intenta dividir entre cero
                raise ValueError("No se puede dividir entre cero.")
            return self.valor1 / self.valor2
        else:
            return 0

    def save(self, *args, **kwargs):
        # Calculamos el resultado antes de guardar
        self.resultado = self.calcular_resultado()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_tipo_display()} de {self.valor1} y {self.valor2} = {self.resultado}"