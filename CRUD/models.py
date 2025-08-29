from django.db import models

class TipoPersona(models.Model):
    tipoPersona = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoPersona

class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)
    descripcionRol = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombreRol} - {self.descripcionRol}"

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    def __str__(self):
        return self.estado

class EstadoEmpleado(models.Model):
    estadoEmpleado = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoEmpleado

class TipoDocumento(models.Model):
    tipoDocumento = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoDocumento

class Genero(models.Model):
    genero = models.CharField(max_length=50)
    def __str__(self):
        return self.genero

class EstadoCivil(models.Model):
    estadoCivil = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoCivil

class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nacionalidad

class TipoContrato(models.Model):
    tipoContrato = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoContrato

class JornadaLaboral(models.Model):
    jornadaLaboral = models.CharField(max_length=100)
    def __str__(self):
        return self.jornadaLaboral

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100)
    def __str__(self):
        return self.nombreCategoria

class EstadoProducto(models.Model):
    estadoProducto = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoProducto

class TipoMovimiento(models.Model):
    tipoMovimiento = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoMovimiento

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

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=100)
    apellidoPersona = models.CharField(max_length=100)
    idTipoDocumento= models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numeroDocumentoPersona = models.CharField(max_length=50)
    idTipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    direccionPersona = models.CharField(max_length=200)
    telefonoPersona = models.CharField(max_length=20)
    emailPersona = models.EmailField()
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    registroPersona = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombrePersona} {self.apellidoPersona} ({self.numeroDocumentoPersona})"

class Empleado(models.Model):
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fechaNacimiento = models.DateField()
    idGenero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    idEstadoCivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    idNacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    fechaContratacion = models.DateField()
    idTipoContrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    idJornadaLaboral = models.ForeignKey(JornadaLaboral, on_delete=models.CASCADE)
    salarioEmpleado = models.DecimalField(max_digits=10, decimal_places=2)
    epsEmpleado = models.CharField(max_length=100)
    idEstadoEmpleado = models.ForeignKey(EstadoEmpleado, on_delete=models.CASCADE)
    fotoEmpleado = models.ImageField(upload_to='uploads/fotos_empleados/', null=True, blank=True)
    def __str__(self):
        return f"Empleado: {self.idPersona}"

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

class Cliente(models.Model):
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fechaRegistroCliente = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cliente: {self.idPersona}"

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

class Venta(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    totalValorVenta = models.DecimalField(max_digits=15, decimal_places=2)
    estadoVenta = models.ForeignKey(EstadoVenta, on_delete=models.CASCADE)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Venta a {self.idCliente} por {self.totalValorVenta}"

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