from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Producto, Venta, Detalle, Rol, TipoProducto, ItemCarrito, Carrito, CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'payment_transaction')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle)
admin.site.register(Rol)
admin.site.register(TipoProducto)
admin.site.register(ItemCarrito)
admin.site.register(Carrito)