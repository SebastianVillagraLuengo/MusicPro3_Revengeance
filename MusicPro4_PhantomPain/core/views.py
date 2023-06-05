from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto,TipoProducto,Carrito,ItemCarrito
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, permission_required


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

@login_required
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

@login_required
def vista_usuario(request):
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
    return render(request, 'core/vista_usuario.html',data)
@permission_required('core.add_producto')
def vista_admin(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'core/vista_admin.html', data)


@permission_required('core.add_producto')
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

@permission_required('core.add_producto')
def agregar_productos(request):
    tipo_producto = TipoProducto.objects.all()
    variables ={
        'tipo_producto':tipo_producto
    }

    return render(request, 'core/formularioAgregarProductos.html', variables)

#PARA CUANDO EL FELIPE QL SE DIGNE A HACER LA WEA DE CARRITO @login_required
def carrito(request):
    # Obtener el carrito actual del usuario basado en la sesión
    carrito_actual = Carrito.objects.get(id=request.session['carrito_id'])
    
    # Obtener los elementos del carrito desde la base de datos
    items = ItemCarrito.objects.filter(carrito=carrito_actual)
    
    # Pasar los elementos del carrito al contexto de la plantilla
    context = {'items': items}
    
    return render(request, 'core/carrito.html', context)
    
@permission_required('core.add_producto')
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

@permission_required('core.add_producto')
def eliminacion_prod(request, nombreProducto):
    producto = Producto.objects.get(nombreProducto = nombreProducto)
    producto.delete()
    messages.success(request, 'Producto eliminado con éxito')

    return redirect('tienda_admin')

@permission_required('core.add_producto')
def modificar_productos(request, id):
    producto = get_object_or_404(Producto, pk=id)
    tipo_producto = TipoProducto.objects.all()

    if request.method == 'POST':
        producto.nombreProducto = request.POST.get('nomProd')
        producto.descripcionProducto = request.POST.get('descripcionProducto')
        producto.precioProducto = request.POST.get('precioProducto')
        producto.stockProducto = request.POST.get('stockProducto')
        producto.tipoNombre_id = request.POST.get('tipo_producto')

        # Actualizar las imágenes solo si se proporcionan nuevos archivos
        if 'imagenUno' in request.FILES:
            producto.imagenUno = request.FILES['imagenUno']
        if 'imagenDos' in request.FILES:
            producto.imagenDos = request.FILES['imagenDos']
        if 'imagenTres' in request.FILES:
            producto.imagenTres = request.FILES['imagenTres']
        if 'imagenCuatro' in request.FILES:
            producto.imagenCuatro = request.FILES['imagenCuatro']

        producto.save()
        return redirect('tienda_admin')
    
    return render(request, 'core/modificarProductos.html', {'producto': producto, 'tipo_producto': tipo_producto})

def funcion_login(request):
    if request.method == 'POST':
        username = request.POST['nombre']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.has_perm('core.add_producto'):      
                 return redirect('vista_admin')
            else:
                 return redirect('vista_usuario') # Cambia 'vista_usuario' con el nombre de tu vista principal

        else:
            messages.error(request, 'El usuario y/o contraseña no coinciden o no existen.')
            return render(request, 'core/formularioLogin.html')
            
    return render(request, 'core/formularioLogin.html')

@csrf_protect
def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        celular = request.POST['celular']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']

        if password == repeat_password:
            try:
                # Crea un nuevo usuario utilizando la tabla User de Django
                user = User.objects.create_user(username=email, password=password)
                # Agrega los campos personalizados al usuario
                user.first_name = nombre
                user.last_name = apellido
                user.email = email
                user.save()
                # Inicia sesión automáticamente después del registro
                user = authenticate(request, username=email, password=password)
                login(request, user)
                return redirect('login')  # Redirige a la página de inicio después del registro exitoso
            except Exception as e:
                messages.error(request, f'Error al registrar el usuario: {str(e)}')
        else:
            messages.error(request, 'Las contraseñas no coinciden')

    return render(request, 'core/formularioRegistro.html')


def mostrar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    return render(request, 'core/producto.html', {'producto': producto})

@login_required
def agregar_al_carrito(request, id):
    # Obtener el producto utilizando el ID recibido
    producto = get_object_or_404(Producto, id=id)

    # Verificar si el carrito ya existe en la sesión
    if 'carrito_id' in request.session:
        # Obtener el carrito existente utilizando el carrito_id almacenado en la sesión
        carrito = get_object_or_404(Carrito, id=request.session['carrito_id'])
    else:
        # Si el carrito no existe en la sesión, crear uno nuevo y almacenar su ID en la sesión
        carrito = Carrito.objects.create(usuario=request.user)
        request.session['carrito_id'] = carrito.id

    # Crear una instancia del modelo ItemCarrito con el producto, el carrito y la cantidad
    cantidad = int(request.POST.get('cantidad'))  # Cambia este valor según tus necesidades
    item_carrito = ItemCarrito(carrito=carrito, producto=producto, cantidad=cantidad)

    # Guardar el nuevo item del carrito
    item_carrito.save()

    # Redirigir al usuario a la página del carrito o a la página de la tienda
    return redirect('carrito')  # Ajusta el nombre de la URL según corresponda

def actualizar_cantidad(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('productId')
        quantity = request.POST.get('quantity')
        item = ItemCarrito.objects.get(pk=product_id)
        item.cantidad_actualizada = int(quantity)  # Actualizar el valor de cantidad_actualizada
        item.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})