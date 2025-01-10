from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_operacion, name='crear_operacion'),
    path('detalle/<int:pk>/', views.detalle_operacion, name='detalle_operacion'),
]
