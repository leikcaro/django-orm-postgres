from django.shortcuts import render, redirect, get_object_or_404
from .models import Operacion
from .forms import OperacionForm

def crear_operacion(request):
    """
    Vista que permite crear una op. aritmética mediante un formulario.
    """
    if request.method == 'POST':
        form = OperacionForm(request.POST)
        if form.is_valid():
            operacion = form.save() 
            return redirect('detalle_operacion', pk=operacion.pk)
    else:
        form = OperacionForm()

    return render(request, 'calculadora/crear_operacion.html', {'form': form})


def detalle_operacion(request, pk):
    """
    Vista de detalle de una op. en particular que muestra su resultado.
    """
    operacion = get_object_or_404(Operacion, pk=pk)
    return render(request, 'calculadora/detalle_operacion.html', {'operacion': operacion})

