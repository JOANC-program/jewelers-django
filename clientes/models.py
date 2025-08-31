from django.db import models
from personas.models import Persona
from core.models import Estado

# Create your models here.

class Cliente(models.Model):
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    fechaRegistroCliente = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Cliente: {self.idPersona}"