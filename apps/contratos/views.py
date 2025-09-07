from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contrato


@login_required
def listar_contratos(request):
    contratos = Contrato.objects.select_related('cliente').order_by('-fecha_inicio')
    return render(request, 'contratos/listar.html', {'contratos': contratos})


@login_required
def crear_contrato(request):
    if request.method == 'POST':
        messages.success(request, 'Contrato creado exitosamente.')
        return redirect('contratos:listar')
    return render(request, 'contratos/crear.html')


@login_required
def detalle_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    return render(request, 'contratos/detalle.html', {'contrato': contrato})


@login_required
def editar_contrato(request, pk):
    contrato = get_object_or_404(Contrato, pk=pk)
    if request.method == 'POST':
        messages.success(request, 'Contrato actualizado exitosamente.')
        return redirect('contratos:detalle', pk=contrato.pk)
    return render(request, 'contratos/editar.html', {'contrato': contrato})