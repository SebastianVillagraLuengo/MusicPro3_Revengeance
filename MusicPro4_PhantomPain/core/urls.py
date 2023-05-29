from django.contrib import admin
from django.urls import path
from .views import home,producto,html_registro,html_login,tienda,vista_usuario,vista_admin,tienda_admin,agregar_productos


urlpatterns = [
    path('', home, name='index'),
    path('producto', producto, name='producto'),
    path('Registro', html_registro, name='Registro'),
    path('Login', html_login, name='Login'),
    path('tienda', tienda, name='tienda'),
    path('Usuario', vista_usuario, name='vista_usuario'),
    path('admin', vista_admin, name='vista_admin'),
    path('tienda_admin', tienda_admin, name='tienda_admin'),
    path('agregar_productos', agregar_productos, name='agregar_productos'),
]