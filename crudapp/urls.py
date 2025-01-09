from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.insertar_emp, name = 'insertar-emp'),
    path('mostrar/', views.mostrar_emp, name='mostrar-emp'),
    path('editar/<int:pk>', views.editar_emp, name='editar-emp'),
    path('editar/actualizarempleado/<int:id>', views.actualizarempleado,
name='actualizarempleado'),

    path('eliminar/<int:pk>', views.eliminar_emp, name='eliminar-emp'),
]
