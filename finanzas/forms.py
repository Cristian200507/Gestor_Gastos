from django import forms
from .models import Gasto, Ingreso

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['categoria', 'descripcion', 'monto']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe el gasto'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 25000'}),
        }
        labels = {
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'monto': 'Monto ($)',
        }

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['categoria', 'descripcion', 'monto']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Describe el ingreso'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 150000'}),
        }
        labels = {
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'monto': 'Monto ($)',
        }
