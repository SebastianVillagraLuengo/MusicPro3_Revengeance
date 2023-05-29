from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')
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
    return render(request, 'core/formularioAgregarProductos.html')

def carrito(request):
    return render(request, 'core/carrito.html')