from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Pedido, TipoServicio, EstadoPedido


@login_required
def listar_pedidos(request):
    """Vista para listar pedidos"""
    
    pedidos = Pedido.objects.select_related('cliente').order_by('-fecha_pedido')
    
    # Filtros
    busqueda = request.GET.get('busqueda', '')
    estado_filtro = request.GET.get('estado', '')
    servicio_filtro = request.GET.get('servicio', '')
    
    if busqueda:
        pedidos = pedidos.filter(
            Q(numero_pedido__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda) |
            Q(cliente__razon_social__icontains=busqueda)
        )
    
    if estado_filtro:
        pedidos = pedidos.filter(estado=estado_filtro)
    
    if servicio_filtro:
        pedidos = pedidos.filter(tipo_servicio=servicio_filtro)
    
    # Paginación
    paginator = Paginator(pedidos, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'busqueda': busqueda,
        'estado_filtro': estado_filtro,
        'servicio_filtro': servicio_filtro,
        'estados': EstadoPedido.choices,
        'servicios': TipoServicio.choices,
    }
    
    return render(request, 'pedidos/listar.html', context)


@login_required
def crear_pedido(request):
    """Vista para crear un nuevo pedido"""
    
    if request.method == 'POST':
        # Procesar formulario (implementar después)
        messages.success(request, 'Pedido creado exitosamente.')
        return redirect('pedidos:listar')
    
    context = {
        'servicios': TipoServicio.choices,
        'estados': EstadoPedido.choices,
    }
    
    return render(request, 'pedidos/crear.html', context)


@login_required
def detalle_pedido(request, pk):
    """Vista para ver detalles de un pedido"""
    
    pedido = get_object_or_404(Pedido, pk=pk)
    
    context = {
        'pedido': pedido,
    }
    
    return render(request, 'pedidos/detalle.html', context)


@login_required
def editar_pedido(request, pk):
    """Vista para editar un pedido"""
    
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if request.method == 'POST':
        # Procesar formulario (implementar después)
        messages.success(request, 'Pedido actualizado exitosamente.')
        return redirect('pedidos:detalle', pk=pedido.pk)
    
    context = {
        'pedido': pedido,
        'servicios': TipoServicio.choices,
        'estados': EstadoPedido.choices,
    }
    
    return render(request, 'pedidos/editar.html', context)


@login_required
def eliminar_pedido(request, pk):
    """Vista para eliminar un pedido"""
    
    pedido = get_object_or_404(Pedido, pk=pk)
    
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, 'Pedido eliminado exitosamente.')
        return redirect('pedidos:listar')
    
    context = {
        'pedido': pedido,
    }
    
    return render(request, 'pedidos/eliminar.html', context)