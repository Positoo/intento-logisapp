from django.shortcuts import render, redirect

from .models import Remito
from .forms import RemitoForm

def lista_remitos(request):
    remitos = Remito.objects.all()

    return render(request, 'remitos/lista_remitos.html', {'remitos': remitos})


#Mostrar el formulario para carga de remitos

def crear_remito(request):
    if request.method == 'POST':
        form = RemitoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_remitos')
    else:
        form = RemitoForm()

    return render(request, 'remitos/crear_remito.html', {'form': form})
