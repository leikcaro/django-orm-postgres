from django import forms
from .models import Operacion

class OperacionForm(forms.ModelForm):
    """
    Formulario para crear una Operación (suma, resta, multiplicación, división).
    """
    class Meta:
        model = Operacion
        fields = ['tipo', 'valor1', 'valor2']
