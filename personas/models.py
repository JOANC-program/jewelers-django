from django.db import models
from core.models import Estado
estado_activo, created = Estado.objects.get_or_create(estado="Activo")
print(estado_activo.id)

# Create your models here.

class TipoPersona(models.Model):
    tipoPersona = models.CharField(max_length=100)
    def __str__(self):
        return self.tipoPersona

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

class Persona(models.Model):
    nombrePersona = models.CharField(max_length=100)
    apellidoPersona = models.CharField(max_length=100)
    idTipoDocumento= models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numeroDocumentoPersona = models.CharField(max_length=50)
    idTipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    direccionPersona = models.CharField(max_length=200)
    telefonoPersona = models.CharField(max_length=20)
    emailPersona = models.EmailField()
    idGenero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    registroPersona = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombrePersona} {self.apellidoPersona} ({self.numeroDocumentoPersona})"


