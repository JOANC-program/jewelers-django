from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        widgets = {
            
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'stock': 'Cantidad en Stock',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del producto.',
            'descripcion': 'Proporcione una descripción detallada del producto.',
            'precio': 'Establezca el precio del producto en USD.',
            'stock': 'Indique la cantidad disponible en inventario.',
        }
        error_messages = {
            'nombre': {
                'max_length': 'El nombre es demasiado largo.',
                'required': 'El nombre es obligatorio.',
            },
            'precio': {
                'invalid': 'Ingrese un precio válido.',
                'required': 'El precio es obligatorio.',
            },
            'stock': {
                'invalid': 'Ingrese una cantidad válida.',
                'required': 'La cantidad en stock es obligatoria.',
            },
        }