from django.shortcuts import render, redirect
from .models import *

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
    pass

def editar_emp(request):
    pass

def eliminar_emp(request):
    pass

