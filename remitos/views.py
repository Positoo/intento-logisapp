from django.shortcuts import render, redirect, get_object_or_404

from .models import Remito, HojaDeRuta, HojaDeRutaDetalle
from .forms import RemitoForm, HojaDeRutaForm

#Pagina principal para poder acceder a las demas paginas
def home(request):
    return render(request, 'home.html')


#Remitos
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

#------------------------------HOJAS DE RUTA---------------------------------#

def lista_hojas_ruta(request):
    listaHojas = HojaDeRuta.objects.all()

    return render(request, 'remitos/lista_hojas.html', {'hojas': listaHojas})

#Crear hoja de ruta

def crear_hoja(request):
    if request.method == 'POST':
        form = HojaDeRutaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_hojas')
    else:
        form = HojaDeRutaForm()
        
    return render(request, 'remitos/crear_hoja.html', {'form': form})

#----------------DETALLES DE LA HOJA DE RUTA--------------------

def detalle_hoja(request, id):
    hoja = get_object_or_404(HojaDeRuta, id=id)  #Obtiene la hoja que se va a repetir en los remitos asigandos a ella.

    if request.method == 'POST':
        remito_id = request.POST.get('remito_id')  #Obtiene el id del remito que va a agregar a la hoja de ruta.
        remito = get_object_or_404(Remito, id=remito_id)  #Obtiene el remito.

        detalles = HojaDeRutaDetalle.objects.filter(hoja_ruta=hoja) #Obtiene todos los detalles de esa hoja de ruta y los va a utilizar para contarlos y saber cual seria el ultimo elemento para el orden del nuevo remito(detalle) agrgado.
        orden_ultimo = detalles.count() + 1

        # crear relación
        HojaDeRutaDetalle.objects.create(
            hoja_ruta=hoja,
            remito=remito,
            orden=orden_ultimo
        )

        # cambiar estado del remito
        remito.estado = 'en_ruta'
        remito.save()

        return redirect('detalle_hoja', id=id)

    detalles = HojaDeRutaDetalle.objects.filter(hoja_ruta=hoja)
    remitos_disponibles = Remito.objects.filter(estado='pendiente')

    return render(request, 'remitos/detalle_hoja.html', {
        'hoja': hoja,
        'detalles': detalles,
        'remitos_disponibles': remitos_disponibles
    })