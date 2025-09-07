from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EventoAgenda


@login_required
def listar_eventos(request):
    eventos = EventoAgenda.objects.all().order_by('fecha_inicio')
    return render(request, 'agenda/listar.html', {'eventos': eventos})


@login_required
def crear_evento(request):
    return render(request, 'agenda/crear.html')


@login_required
def detalle_evento(request, pk):
    evento = get_object_or_404(EventoAgenda, pk=pk)
    return render(request, 'agenda/detalle.html', {'evento': evento})