from django.db import models
from empleados.models import Empleado
from personas.models import Persona, TipoPersona
from core.models import Estado
# Create your models here.


class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreCategoria

class EstadoProducto(models.Model):
    estadoProducto = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoProducto

class Producto(models.Model):
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=200)
    stockProducto = models.PositiveBigIntegerField()
    precioProducto = models.DecimalField(max_digits=10, decimal_places=2)
    fechaIngresoProducto = models.DateTimeField(auto_now_add=True)
    idEstadoProducto = models.ForeignKey(EstadoProducto, on_delete=models.CASCADE)
    fotoProducto = models.ImageField(upload_to='uploads/fotos_productos/', null=True, blank=True)
    def __str__(self):
        return f"{self.nombreProducto} ({self.idCategoria})"



class TipoMovimiento(models.Model):
    tipoMovimiento = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoMovimiento

class Proveedor(models.Model):
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idTipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    direccionProveedor = models.CharField(max_length=200)
    telefonoProveedor = models.CharField(max_length=20)
    emailProveedor = models.EmailField()
    fechaRegistroProveedor = models.DateTimeField(auto_now_add=True)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    def __str__(self):
        return f"Proveedor: {self.idPersona}"

class Movimiento(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True, blank=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    codigoMovimiento = models.CharField(max_length=50)
    precioCompraUnidad = models.DecimalField(max_digits=10, decimal_places=2)
    precioVentaUnidad = models.DecimalField(max_digits=10, decimal_places=2)
    cantidadProductoMovimiento = models.PositiveBigIntegerField()
    totalValorMovimiento = models.DecimalField(max_digits=15, decimal_places=2)
    tipoMovimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
    observacionMovimiento = models.CharField(max_length=200, null=True, blank=True)
    fechaMovimiento = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Movimiento {self.codigoMovimiento} ({self.tipoMovimiento})"