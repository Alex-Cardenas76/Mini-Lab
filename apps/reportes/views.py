from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ReporteGenerado, MetricaFinanciera


@login_required
def dashboard_reportes(request):
    reportes_recientes = ReporteGenerado.objects.all().order_by('-fecha_generacion')[:10]
    return render(request, 'reportes/dashboard.html', {'reportes_recientes': reportes_recientes})


@login_required
def reportes_financieros(request):
    metricas = MetricaFinanciera.objects.all().order_by('-fecha')[:12]
    return render(request, 'reportes/financieros.html', {'metricas': metricas})


@login_required
def reportes_inventario(request):
    return render(request, 'reportes/inventario.html')


@login_required
def reportes_produccion(request):
    return render(request, 'reportes/produccion.html')