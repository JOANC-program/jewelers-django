from django.contrib import admin
from .models import TipoPersona, TipoDocumento, Genero, EstadoCivil, Nacionalidad, Persona
admin.site.register(TipoPersona)
admin.site.register(TipoDocumento)  
admin.site.register(Genero)
admin.site.register(EstadoCivil)
admin.site.register(Nacionalidad)
admin.site.register(Persona)
# Register your models here.
