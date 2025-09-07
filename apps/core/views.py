from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
import json

# Importar modelos necesarios
from apps.pedidos.models import Pedido, TipoServicio, EstadoPedido
from apps.inventario.models import Varilla
from apps.inventario.models_extended import PinturaAcabado, MaterialImpresion, MaterialRecordatorio
from apps.produccion.models import OrdenProduccion


@login_required
def dashboard_view(request):
    """Vista del dashboard principal"""
    
    # Datos básicos para demo (sin consultas complejas por ahora)
    estadisticas = {
        'pedidos_nuevos': 0,
        'pedidos_entregados': 0,
        'ordenes_produccion': 0,
        'stock_bajo': 0,
    }
    
    # Datos vacíos por ahora
    alertas_inventario = []
    pedidos_recientes = []
    ingresos_por_servicio = {'labels': [], 'data': []}
    
    context = {
        'estadisticas': estadisticas,
        'alertas_inventario': alertas_inventario,
        'pedidos_recientes': pedidos_recientes,
        'ingresos_por_servicio': json.dumps(ingresos_por_servicio),
    }
    
    return render(request, 'dashboard/index.html', context)


def login_view(request):
    """Vista de login personalizada"""
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Establecer tenant_id en la sesión (por ahora usar uno por defecto)
                request.session['tenant_id'] = 'default_tenant'
                
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor complete todos los campos.')
    
    return render(request, 'auth/login.html')


def logout_view(request):
    """Vista de logout"""
    logout(request)
    messages.info(request, 'Sesión cerrada exitosamente.')
    return redirect('login')


def get_items_stock_bajo_count():
    """Cuenta los items con stock bajo en todas las categorías"""
    count = 0
    
    # Varillas
    count += Varilla.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).count()
    
    # Pinturas
    count += PinturaAcabado.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).count()
    
    # Materiales de impresión
    count += MaterialImpresion.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).count()
    
    # Materiales de recordatorio
    count += MaterialRecordatorio.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).count()
    
    return count


def get_alertas_inventario():
    """Obtiene las alertas de inventario más críticas"""
    alertas = []
    
    # Varillas con stock bajo
    varillas_stock_bajo = Varilla.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).order_by('stock_actual')[:5]
    
    for varilla in varillas_stock_bajo:
        alertas.append({
            'tipo': 'Varilla',
            'producto': varilla.nombre,
            'stock_actual': varilla.stock_actual,
            'stock_minimo': varilla.stock_minimo,
        })
    
    # Pinturas con stock bajo
    pinturas_stock_bajo = PinturaAcabado.objects.filter(
        stock_actual__lte=models.F('stock_minimo')
    ).order_by('stock_actual')[:3]
    
    for pintura in pinturas_stock_bajo:
        alertas.append({
            'tipo': 'Pintura/Acabado',
            'producto': pintura.nombre,
            'stock_actual': pintura.stock_actual,
            'stock_minimo': pintura.stock_minimo,
        })
    
    return alertas


def get_ingresos_por_servicio():
    """Calcula los ingresos por tipo de servicio para el gráfico"""
    
    # Obtener pedidos del último mes
    fecha_limite = timezone.now() - timedelta(days=30)
    
    ingresos = Pedido.objects.filter(
        fecha_pedido__gte=fecha_limite,
        estado=EstadoPedido.ENTREGADO
    ).values('tipo_servicio').annotate(
        total=models.Sum('monto_total')
    )
    
    # Formatear para Chart.js
    labels = []
    data = []
    
    for ingreso in ingresos:
        # Obtener el nombre legible del servicio
        servicio = dict(TipoServicio.choices).get(ingreso['tipo_servicio'], ingreso['tipo_servicio'])
        labels.append(servicio)
        data.append(float(ingreso['total'] or 0))
    
    return {
        'labels': labels,
        'data': data
    }


@login_required
def configuracion_view(request):
    """Vista de configuración (placeholder)"""
    return render(request, 'configuracion.html')


# Importar models y funciones de Django
from django.db import models