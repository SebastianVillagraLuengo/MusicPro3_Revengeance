from django.db import models
from datetime import date

# Create your models here.

#Tabla de roles
class Rol(models.Model):
    nombreRol= models.CharField(max_length=25,verbose_name='El nombre del rol de usuario')
    def __str__(self) -> str:
        return self.nombreRol

#Tabla de usuario
class Usuario(models.Model):
    #llave primaria
    nombreUsuario = models.CharField(max_length=25,verbose_name='El nombre que el usuario usa para ingresar a su cuenta')
    apellidos = models.CharField(max_length=25,verbose_name='El nombre que se mostrara algún día en la sección de comentarios')
    correoUsuario = models.CharField(max_length=25,verbose_name='El correo asociado a la cuenta')
    celular = models.IntegerField(verbose_name='El correo asociado a la cuenta')
    clave = models.CharField(max_length=25,verbose_name='El correo asociado a la cuenta')

    #llave foranea
    rol=models.ForeignKey(Rol,on_delete=models.PROTECT,verbose_name='La llave de rol-usuario')

    def __str__(self) -> str:
        return self.nombreUsuario

#Tabla de modelos3d
class Producto(models.Model):
    #Llave primaria
    nombreProducto = models.CharField(max_length=25,verbose_name='El nombre asociado al producto')
    descripcionProducto = models.CharField(max_length=2000,verbose_name='La descripción asociada al producto en cuestión')
    precioProducto = models.IntegerField(verbose_name='El precio asociado al producto')
    stockProducto = models.IntegerField(verbose_name='El stock asociado al producto')
    imagenUno= models.ImageField(upload_to="CarpetaDestino",verbose_name='Primera imagen')
    imagenDos= models.ImageField(upload_to="CarpetaDestino",verbose_name='Segunda imagen')
    imagenTres= models.ImageField(upload_to="CarpetaDestino",verbose_name='Tercera imagen')
    imagenCuatro= models.ImageField(upload_to="CarpetaDestino",verbose_name='Cuarta imagen')
    
    def __str__(self) -> str:
        return self.nombreProducto

#Tabla de ventas
class Venta(models.Model):
    #LLave primariaforanea
    #fecha
    fechaVenta = models.DateField()
    totalVenta= models.IntegerField(verbose_name='El total asociado a la venta despues de el iva de mierda')
    #Llave foranea
    nombreUsuario=models.ForeignKey(Usuario,on_delete=models.PROTECT,verbose_name='llave usuario-venta')

    def __str__(self) -> str:
        return self.fechaVenta

class Detalle(models.Model):
    #Llave primaria
    totalDetalle= models.IntegerField(verbose_name='El total asociado a la venta despues de el iva de mierda')
    #LLAVES foranea
    fechaVenta=models.ForeignKey(Venta,on_delete=models.PROTECT,verbose_name='llave Venta-Detalle')
    nombreProducto=models.ForeignKey(Producto,on_delete=models.PROTECT,verbose_name='llave Venta-Detalle')