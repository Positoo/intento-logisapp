from django import forms
from .models import Remito, HojaDeRuta, HojaDeRutaDetalle

class RemitoForm(forms.ModelForm):
    class Meta:
        model = Remito
        fields = ['cliente', 'consignatario_nombre', 'destino', 'valor_declarado', 'cantidad_bultos']

#Formulario para craer Hoja De Ruta
class HojaDeRutaForm(forms.ModelForm):
    class Meta:
        model = HojaDeRuta
        fields = '__all__'