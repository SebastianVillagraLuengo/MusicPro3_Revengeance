from django.shortcuts import render
from .models import Producto,TipoProducto
from django.contrib import messages

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
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
    return render(request, 'core/tienda.html')

def vista_usuario(request):
    return render(request, 'core/vista_usuario.html')

def vista_admin(request):
    return render(request, 'core/vista_admin.html')

def tienda_admin(request):
    return render(request, 'core/tienda_admin.html')

def agregar_productos(request):

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
        pro.imagenUno = request.POST.get('foto_1')
        pro.imagenDos = request.POST.get('foto_2')
        pro.imagenTres = request.POST.get('foto_3')
        pro.imagenCuatro = request.POST.get('foto_4')

        try:
            pro.save()
            messages.success(request, 'Producto agregado correctamente')
            return redirect('agregar_productos')
        except:
            messages.error(request, 'No se pudo agregar el producto')


    return render(request, 'core/formularioAgregarProductos.html',variables)

def carrito(request):
    return render(request, 'core/carrito.html')