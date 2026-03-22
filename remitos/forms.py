from django import forms
from .models import Remito

class RemitoForm(forms.ModelForm):
    class Meta:
        model = Remito
        fields = ['cliente', 'estado']