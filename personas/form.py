from django import forms 
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombrePersona',
            'apellidoPersona',
            'idTipoDocumento',
            'numeroDocumentoPersona',
            'idTipoPersona',
            'direccionPersona',
            'telefonoPersona',
            'emailPersona',
            'idGenero',
            'idEstado',
        ]
        labels = {
            'nombrePersona': 'Nombres',
            'apellidoPersona': 'Apellidos',
            'idTipoDocumento': 'Tipo de Documento',
            'numeroDocumentoPersona': 'Número de Documento',
            'idTipoPersona': 'Tipo de Persona',
            'direccionPersona': 'Dirección',
            'telefonoPersona': 'Teléfono',
            'emailPersona': 'Correo electrónico',
            'idGenero': 'Género',
            'idEstado': 'Estado',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'