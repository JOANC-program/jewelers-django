from django.db import models
from personas.models import Persona, Genero, EstadoCivil, Nacionalidad
# Create your models here.
class EstadoEmpleado(models.Model):
    estadoEmpleado = models.CharField(max_length=50)
    def __str__(self):
        return self.estadoEmpleado

class TipoContrato(models.Model):
    tipoContrato = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoContrato

class JornadaLaboral(models.Model):
    jornadaLaboral = models.CharField(max_length=100)
    def __str__(self):
        return self.jornadaLaboral
    
class GrupoSanguineo(models.Model):
    grupoSanguineo = models.CharField(max_length=3)
    def __str__(self):
        return self.grupoSanguineo

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
    idGrupoSanguineo = models.ForeignKey(GrupoSanguineo, on_delete=models.CASCADE)
    idEstadoEmpleado = models.ForeignKey(EstadoEmpleado, on_delete=models.CASCADE)
    fotoEmpleado = models.ImageField(upload_to='uploads/fotos_empleados/', null=True, blank=True)
    def __str__(self):
        return f"Empleado: {self.idPersona}"