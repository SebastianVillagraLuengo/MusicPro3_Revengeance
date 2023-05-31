from django.shortcuts import render, redirect
from .models import Producto,TipoProducto
from django.contrib import messages

def home(request):
    productos = Producto.objects.all()
    instrumentos = Producto.objects.filter(tipoNombre='1')
    equipos = Producto.objects.filter(tipoNombre='2')
    accesorios = Producto.objects.filter(tipoNombre='3')
    oferta = Producto.objects.filter(tipoNombre='4')
    bajos = Producto.objects.filter(nombreProducto__icontains='Bajo')
    data = {
        'oferta': oferta,
        'instrumentos': instrumentos,
        'equipos': equipos,
        'accesorios': accesorios,
        'bajos': bajos
    }
    return render(request, 'core/index.html', data)
# Create your views here.
def producto(request):
    return render(request, 'core/producto.html')

def html_registro(request):
    return render(request, 'core/formularioRegistro.html')

def html_login(request):
    return render(request, 'core/formularioLogin.html')

def tienda(request):
    productos = Producto.objects.all()
    instrumentos = Producto.objects.filter(tipoNombre='1')
    equipos = Producto.objects.filter(tipoNombre='2')
    accesorios = Producto.objects.filter(tipoNombre='3')
    oferta = Producto.objects.filter(tipoNombre='4')

    data = {
        'oferta': oferta,
        'instrumentos': instrumentos,
        'equipos': equipos,
        'accesorios': accesorios
    }
    return render(request, 'core/tienda.html', data)

def vista_usuario(request):
    return render(request, 'core/vista_usuario.html')

def vista_admin(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/vista_admin.html', data)


def tienda_admin(request):
    productos = Producto.objects.all()
    instrumentos = Producto.objects.filter(tipoNombre='1')
    equipos = Producto.objects.filter(tipoNombre='2')
    accesorios = Producto.objects.filter(tipoNombre='3')
    oferta = Producto.objects.filter(tipoNombre='4')

    data = {
        'oferta': oferta,
        'instrumentos': instrumentos,
        'equipos': equipos,
        'accesorios': accesorios
    }
    return render(request, 'core/tienda_admin.html', data)

def agregar_productos(request):
    tipo_producto = TipoProducto.objects.all()
    variables ={
        'tipo_producto':tipo_producto
    }

    return render(request, 'core/formularioAgregarProductos.html', variables)

def carrito(request):
    return render(request, 'core/carrito.html')


def formProducto(request):
    tipo_producto = TipoProducto.objects.all()
    variables ={
        'tipo_producto':tipo_producto
    }

    if request.POST:
        pro = Producto()
        pro.nombreProducto = request.POST.get('nomProd')
        pro.descripcionProducto = request.POST.get('descProd')
        pro.precioProducto = request.POST.get('precio')
        pro.stockProducto = request.POST.get('cantidad')
        ti_producto = TipoProducto()
        ti_producto.id = request.POST.get('tipo_producto')
        pro.tipoNombre = ti_producto
        pro.imagenUno = request.FILES.get('foto_1')
        pro.imagenDos = request.FILES.get('foto_2')
        pro.imagenTres = request.FILES.get('foto_3')
        pro.imagenCuatro = request.FILES.get('foto_4')

        try:
            pro.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect('agregar_productos')
        except:
            messages.error(request, 'No se pudo agregar el producto')

    return redirect(request, 'core/formularioAgregarProductos.html')


def eliminacion_prod(request, nombreProducto):
    producto = Producto.objects.get(nombreProducto = nombreProducto)
    producto.delete()
    messages.success(request, 'Producto eliminado con éxito')

    return redirect('tienda_admin')

def modificar_productos(request, id):
    producto = Producto.objects.get(id=id)
    tipo_producto = TipoProducto.objects.all()

    variables = {
        'producto':producto,
        'tipo_producto':tipo_producto
    }

    return render(request, 'core/modificarProductos.html',variables)