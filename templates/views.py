from django.shortcuts import render
from .models import listaServicios, listaDetalles
# Create your views here.

def home(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def servicios(request):
    context = {
        'servicios': listaServicios()
    }
    return render(request, 'servicios.html', context)

def contactos(request):
    return render(request, 'contacto.html')

def detalle(request, servicio_id):
    detalles = {d.numero_Servicio: d for d in listaDetalles()}
    detalle_data = detalles.get(servicio_id)
    if detalle_data:
        return render(request, 'detalle.html', {'detalle': detalle_data})
    return render(request, 'index.html')



