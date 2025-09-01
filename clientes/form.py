from django import forms
from .models import Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['idPersona', 'idEstado']
        labels = {
            'idPersona': 'Persona',
            'idEstado': 'Estado',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'