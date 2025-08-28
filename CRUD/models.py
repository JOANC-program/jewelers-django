from django.db import models

class Tarea(models.Model):
    Tarea = models.CharField(max_length=200)
    def __str__(self):
        return self.Tarea
