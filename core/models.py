from django.db import models

# Create your models here.

class Rol(models.Model):
    nombreRol = models.CharField(max_length=100)
    descripcionRol = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombreRol} - {self.descripcionRol}"

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    def __str__(self):
        return self.estado
        