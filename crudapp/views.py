from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView

# Create your views here.

def insertar_emp(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_nombre = request.POST.get('emp_nombre')
        emp_correo = request.POST.get('emp_correo')
        emp_designacion = request.POST.get('emp_designacion')           
        empleado = Empleado(emp_id=emp_id, emp_nombre=emp_nombre, emp_correo=emp_correo, emp_designacion=emp_designacion)
        if emp_id and emp_nombre and emp_correo and emp_designacion:    
            empleado.save()
            return redirect('mostrar/')
        else:
            print('Datos incorrectos')
            return render(request, 'insertar.html',{'mensaje': 'Datos incorrectos'})    
    else:
        return render(request, 'insertar.html')


def mostrar_emp(request):
    empleados = Empleado.objects.all()
    return render(request, 'mostrar.html', {'empleados': empleados})

def editar_emp(request, pk):
    empleado = Empleado.objects.get(emp_id=pk)
    return render(request, 'editar.html', {'empleado': empleado})

def actualizarempleado(request, id):
    emp_id = request.POST['emp_id']
    emp_nombre = request.POST['emp_nombre']
    emp_correo = request.POST['emp_correo']
    emp_designacion = request.POST['emp_designacion']
    empleado = Empleado.objects.get(id=id)
    empleado.emp_id = emp_id
    empleado.emp_nombre = emp_nombre
    empleado.emp_correo = emp_correo
    empleado.emp_designacion = emp_designacion
    empleado.save()
    return redirect('/crudapp/mostrar')    

def eliminar_emp(request):
    """Eliminar un empleado de la base de datos."""
    pass

class InicioPageView(TemplateView):
    template_name = 'inicio.html'

class AcercaPageView(TemplateView):
    template_name = 'acerca-de.html'