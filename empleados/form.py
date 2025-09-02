from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'idPersona',
            'fechaNacimiento',
            'idEstadoCivil',
            'idNacionalidad',
            'fechaContratacion',
            'idTipoContrato',
            'idJornadaLaboral',
            'salarioEmpleado',
            'epsEmpleado',
            'idGrupoSanguineo',
            'idEstadoEmpleado',
            'fotoEmpleado',
        ]
        labels = {
            'idPersona': 'Persona',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'idEstadoCivil': 'Estado Civil',
            'idNacionalidad': 'Nacionalidad',
            'fechaContratacion': 'Fecha de Contratación',
            'idTipoContrato': 'Tipo de Contrato',
            'idJornadaLaboral': 'Jornada Laboral',
            'salarioEmpleado': 'Salario',
            'epsEmpleado': 'EPS',
            'idGrupoSanguineo': 'Grupo Sanguíneo',
            'idEstadoEmpleado': 'Estado del Empleado',
            'fotoEmpleado': 'Foto del Empleado',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'