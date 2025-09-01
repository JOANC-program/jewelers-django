from django.db import models
from clientes.models import Cliente
from empleados.models import Empleado
from productos.models import Producto
from core.models import Estado
# Create your models here.


class EstadoVenta(models.Model):
    estadoVenta = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoVenta

class EstadoCredito(models.Model):
    estadoCredito = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoCredito

class MetodoPago(models.Model):
    metodoPago = models.CharField(max_length=100)
    def __str__(self):
        return self.metodoPago
        
class Venta(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    totalValorVenta = models.DecimalField(max_digits=15, decimal_places=2)
    estadoVenta = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Venta a {self.idCliente} por {self.totalValorVenta}"


class VentaProducto(models.Model):
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadProducto = models.PositiveBigIntegerField()
    precioVentaUnidad = models.DecimalField(max_digits=10, decimal_places=2)
    subTotalValorProducto = models.DecimalField(max_digits=15, decimal_places=2)
    MetodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    descuentoProducto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    totalValorVenta = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return f"Venta {self.idVenta} - Producto {self.idProducto}"


class VentaCredito(models.Model):
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    numeroCuotas = models.PositiveBigIntegerField()
    valorCuota = models.DecimalField(max_digits=15, decimal_places=2)
    EstadoCredito = models.ForeignKey(EstadoCredito, on_delete=models.CASCADE)
    fechaInicioCredito = models.DateTimeField(auto_now_add=True)
    fechaFinCredito = models.DateTimeField()
    interesCredito = models.DecimalField(max_digits=5, decimal_places=2)
    saldoPendiente = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return f"Crédito de {self.idVenta} ({self.EstadoCredito})"

