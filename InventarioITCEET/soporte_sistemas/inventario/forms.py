from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['numero_placa', 'tipo_equipo', 'marca', 'modelo', 'estado', 'ubicacion','nota', 'disco_duro', 'sistema_operativo']
        
