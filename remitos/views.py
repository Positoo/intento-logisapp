from django.shortcuts import render, redirect, get_object_or_404

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

#Editar remito
def editar_remito(request, id):
    remito = get_object_or_404(Remito, id=id) #este metodo recive un modelo (que es el tipo de objeto que va a devolver) y una condicion (con la que buscara ese objecto)

    if request.method == 'POST':
        form = RemitoForm(request.POST, instance=remito)
        if form.is_valid():
            form.save()
            return redirect('lista_remitos')
    else:
        form = RemitoForm(instance=remito)
    
    return render(request, 'remitos/editar_remito.html', {'form': form})

#Eliminar remito
def eliminar_remito(request, id):
    remito = get_object_or_404(Remito, id=id)

    if request.method == 'POST':
        remito.delete()
        return redirect('lista_remitos')
    
    return render(request, 'remitos/eliminar_remito.html', {'remito': remito})