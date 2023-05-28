from django.contrib import admin
from django.urls import path
from .views import home,producto,html_registro,html_login,tienda


urlpatterns = [
    path('', home, name='index'),
    path('producto', producto, name='producto'),
    path('Registro', html_registro, name='Registro'),
    path('Login', html_login, name='Login'),
    path('tienda', tienda, name='tienda'),
]