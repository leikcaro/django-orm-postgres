from django.urls import path, include
from .views import index

app_name = 'blogsite'

urlpatterns = [

    path('', index, name='index'),
]