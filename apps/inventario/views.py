from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Varilla
from .models_extended import PinturaAcabado, MaterialImpresion, MovimientoInventario


@login_required
def listar_inventario(request):
    return render(request, 'inventario/index.html')


@login_required
def alertas_stock(request):
    from django.db import models
    varillas_stock_bajo = Varilla.objects.filter(stock_actual__lte=models.F('stock_minimo'))
    return render(request, 'inventario/alertas.html', {'varillas_stock_bajo': varillas_stock_bajo})


@login_required
def listar_varillas(request):
    varillas = Varilla.objects.all().order_by('nombre')
    return render(request, 'inventario/varillas.html', {'varillas': varillas})


@login_required
def listar_pinturas(request):
    pinturas = PinturaAcabado.objects.all().order_by('nombre')
    return render(request, 'inventario/pinturas.html', {'pinturas': pinturas})


@login_required
def listar_materiales(request):
    materiales = MaterialImpresion.objects.all().order_by('nombre')
    return render(request, 'inventario/materiales.html', {'materiales': materiales})


@login_required
def listar_movimientos(request):
    movimientos = MovimientoInventario.objects.all().order_by('-fecha_movimiento')
    return render(request, 'inventario/movimientos.html', {'movimientos': movimientos})


from django.db import models