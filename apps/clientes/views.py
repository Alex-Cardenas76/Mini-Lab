from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Cliente, TipoCliente


@login_required
def listar_clientes(request):
    """Vista para listar clientes con filtros y paginación"""
    
    clientes = Cliente.objects.all().order_by('-created_at')
    
    # Filtros
    busqueda = request.GET.get('busqueda', '')
    tipo_filtro = request.GET.get('tipo', '')
    
    if busqueda:
        clientes = clientes.filter(
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(razon_social__icontains=busqueda) |
            Q(dni__icontains=busqueda) |
            Q(ruc__icontains=busqueda)
        )
    
    if tipo_filtro:
        clientes = clientes.filter(tipo=tipo_filtro)
    
    # Paginación
    paginator = Paginator(clientes, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'busqueda': busqueda,
        'tipo_filtro': tipo_filtro,
        'tipos_cliente': TipoCliente.choices,
    }
    
    return render(request, 'clientes/listar.html', context)


@login_required
def crear_cliente(request):
    """Vista para crear un nuevo cliente"""
    
    if request.method == 'POST':
        # Procesar formulario (implementar después)
        messages.success(request, 'Cliente creado exitosamente.')
        return redirect('clientes:listar')
    
    context = {
        'tipos_cliente': TipoCliente.choices,
    }
    
    return render(request, 'clientes/crear.html', context)


@login_required
def detalle_cliente(request, pk):
    """Vista para ver detalles de un cliente"""
    
    cliente = get_object_or_404(Cliente, pk=pk)
    
    # Obtener pedidos del cliente
    pedidos = cliente.pedidos.all().order_by('-fecha_pedido')[:10]
    
    context = {
        'cliente': cliente,
        'pedidos': pedidos,
    }
    
    return render(request, 'clientes/detalle.html', context)


@login_required
def editar_cliente(request, pk):
    """Vista para editar un cliente"""
    
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        # Procesar formulario (implementar después)
        messages.success(request, 'Cliente actualizado exitosamente.')
        return redirect('clientes:detalle', pk=cliente.pk)
    
    context = {
        'cliente': cliente,
        'tipos_cliente': TipoCliente.choices,
    }
    
    return render(request, 'clientes/editar.html', context)


@login_required
def eliminar_cliente(request, pk):
    """Vista para eliminar un cliente"""
    
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('clientes:listar')
    
    context = {
        'cliente': cliente,
    }
    
    return render(request, 'clientes/eliminar.html', context)