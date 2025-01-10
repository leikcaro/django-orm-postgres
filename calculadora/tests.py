from django.test import TestCase
from django.urls import reverse
from .models import Operacion

class OperacionModelTest(TestCase):
    def test_suma(self):
        operacion = Operacion.objects.create(tipo='S', valor1=10, valor2=5)
        self.assertEqual(operacion.resultado, 15, "La suma de 10 y 5 debe ser 15")

    def test_resta(self):
        operacion = Operacion.objects.create(tipo='R', valor1=10, valor2=3)
        self.assertEqual(operacion.resultado, 7, "La resta de 10 y 3 debe ser 7")

    def test_multiplicacion(self):
        operacion = Operacion.objects.create(tipo='M', valor1=3, valor2=4)
        self.assertEqual(operacion.resultado, 12, "La multiplicación de 3 y 4 debe ser 12")

    def test_division(self):
        operacion = Operacion.objects.create(tipo='D', valor1=20, valor2=5)
        self.assertEqual(operacion.resultado, 4, "La división de 20 / 5 debe ser 4")

    def test_division_por_cero(self):
        """
        Se espera que al guardar una operación de división por cero, levante ValueError.
        """
        with self.assertRaises(ValueError):
            Operacion.objects.create(tipo='D', valor1=10, valor2=0)

##### Pruebas de vistas ####

class OperacionViewTest(TestCase):
    def test_crear_operacion_suma_via_view(self):
        """
        Envía una petición POST para crear una operación de suma y verifica que se guarde correctamente.
        """
        response = self.client.post(reverse('crear_operacion'), {
            'tipo': 'S',
            'valor1': '10.00',
            'valor2': '5.00'
        })
        # Verificamos que la vista redirija correctamente (302 = redirect).
        self.assertEqual(response.status_code, 302)

        nueva_operacion = Operacion.objects.last()
        self.assertIsNotNone(nueva_operacion, "La operación debería haberse creado.")
        self.assertEqual(nueva_operacion.resultado, 15)

    def test_detalle_operacion(self):
        """
        Crea una operación y luego accede a su vista de detalle, comprobando que los datos son correctos.
        """
        operacion = Operacion.objects.create(tipo='M', valor1=2, valor2=8)
        url = reverse('detalle_operacion', kwargs={'pk': operacion.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "16")  # La multiplicación de 2 * 8 es 16
