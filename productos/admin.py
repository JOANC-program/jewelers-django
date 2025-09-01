from django.contrib import admin
from .models import Producto, EstadoProducto, Categoria
admin.site.register(Producto)
admin.site.register(EstadoProducto)
admin.site.register(Categoria)