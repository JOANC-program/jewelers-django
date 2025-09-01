from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'idPersona',
            'fechaNacimiento',
            'idGenero',
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