from django.shortcuts import render
from .models import listaServicios
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
# HECHO CON IA
def detalle(request, servicio_id):
    servicios = listaServicios()
    detalle_data = next((s for s in servicios if s.id == servicio_id), None)
    if detalle_data:
        return render(request, 'detalle.html', {'servicios': detalle_data})
    return render(request, 'index.html')

