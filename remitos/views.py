from django.shortcuts import render

from .models import Remito

def lista_remitos(request):
    remitos = Remito.objects.all()

    return render(request, 'remitos/lista_remitos.html', {'remitos': remitos})
