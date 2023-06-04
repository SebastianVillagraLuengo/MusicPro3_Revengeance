from django.contrib import admin
from django.urls import path
from .views import home,producto,html_registro,html_login,tienda,vista_usuario,vista_admin,tienda_admin,agregar_productos,carrito, formProducto \
    ,  eliminacion_prod,modificar_productos,funcion_login,registro_view,mostrar_producto


urlpatterns = [
    path('', home, name='index'),
    path('registro', html_registro, name='registro'),
    path('login', html_login, name='login'),
    path('tienda', tienda, name='tienda'),
    path('usuario', vista_usuario, name='vista_usuario'),
    path('vista_admin', vista_admin, name='vista_admin'),
    path('tienda_admin', tienda_admin, name='tienda_admin'),
    path('agregar_productos', agregar_productos, name='agregar_productos'),
    path('carrito', carrito, name='carrito'),
    path('formProducto', formProducto, name='formProducto'),
    path('eliminacion_prod/<nombreProducto>', eliminacion_prod, name='eliminacion_prod'),
    path('modificar_productos/<id>', modificar_productos, name='modificar_productos'),
    path('funcion_login',funcion_login,name='funcion_login'),
    path('registro_view',registro_view,name='registro_view'),
    path('producto/<id>/',mostrar_producto, name='mostrar_producto'),

]