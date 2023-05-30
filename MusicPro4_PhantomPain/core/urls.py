from django.contrib import admin
from django.urls import path
from .views import home,producto,html_registro,html_login,tienda,vista_usuario,vista_admin,tienda_admin,agregar_productos,carrito


urlpatterns = [
    path('', home, name='index'),
    path('producto', producto, name='producto'),
    path('registro', html_registro, name='Registro'),
    path('login', html_login, name='Login'),
    path('tienda', tienda, name='tienda'),
    path('usuario', vista_usuario, name='vista_usuario'),
    path('vista_admin', vista_admin, name='vista_admin'),
    path('tienda_admin', tienda_admin, name='tienda_admin'),
    path('agregar_productos', agregar_productos, name='agregar_productos'),
    path('carrito', carrito, name='carrito'),
]