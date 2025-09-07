from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrdenProduccion, Cuadro


@login_required
def listar_ordenes(request):
    ordenes = OrdenProduccion.objects.all().order_by('-created_at')
    return render(request, 'produccion/listar.html', {'ordenes': ordenes})


@login_required
def crear_orden(request):
    return render(request, 'produccion/crear.html')


@login_required
def detalle_orden(request, pk):
    orden = get_object_or_404(OrdenProduccion, pk=pk)
    return render(request, 'produccion/detalle.html', {'orden': orden})


@login_required
def productos_terminados(request):
    productos = Cuadro.objects.all().order_by('-created_at')
    return render(request, 'produccion/productos_terminados.html', {'productos': productos})