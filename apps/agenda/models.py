from django.db import models
from django.core.validators import MinValueValidator
from apps.core.models import BaseModel
from apps.clientes.models import Cliente


class TipoEvento(models.TextChoices):
    SESION_FOTOS = 'SESION_FOTOS', 'Sesión de Fotos'
    ENTREGA = 'ENTREGA', 'Entrega'
    REUNION = 'REUNION', 'Reunión'
    RECORDATORIO = 'RECORDATORIO', 'Recordatorio'
    MANTENIMIENTO = 'MANTENIMIENTO', 'Mantenimiento'
    OTRO = 'OTRO', 'Otro'


class EstadoEvento(models.TextChoices):
    PROGRAMADO = 'PROGRAMADO', 'Programado'
    CONFIRMADO = 'CONFIRMADO', 'Confirmado'
    EN_PROCESO = 'EN_PROCESO', 'En Proceso'
    COMPLETADO = 'COMPLETADO', 'Completado'
    CANCELADO = 'CANCELADO', 'Cancelado'
    REPROGRAMADO = 'REPROGRAMADO', 'Reprogramado'


class Prioridad(models.TextChoices):
    BAJA = 'BAJA', 'Baja'
    MEDIA = 'MEDIA', 'Media'
    ALTA = 'ALTA', 'Alta'
    URGENTE = 'URGENTE', 'Urgente'


class EventoAgenda(BaseModel):
    """Eventos programados en la agenda"""
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    tipo_evento = models.CharField(
        max_length=20, choices=TipoEvento.choices, verbose_name="Tipo de Evento"
    )
    estado = models.CharField(
        max_length=20, choices=EstadoEvento.choices, default=EstadoEvento.PROGRAMADO, verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=10, choices=Prioridad.choices, default=Prioridad.MEDIA, verbose_name="Prioridad"
    )
    
    # Fechas y horarios
    fecha_inicio = models.DateTimeField(verbose_name="Fecha y Hora de Inicio")
    fecha_fin = models.DateTimeField(verbose_name="Fecha y Hora de Fin")
    es_todo_el_dia = models.BooleanField(default=False, verbose_name="Es Todo el Día")
    
    # Participantes
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, null=True, blank=True,
        related_name='eventos_agenda', verbose_name="Cliente"
    )
    responsable = models.CharField(max_length=100, verbose_name="Responsable")
    participantes = models.TextField(blank=True, verbose_name="Otros Participantes")
    
    # Ubicación
    ubicacion = models.CharField(max_length=200, blank=True, verbose_name="Ubicación")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    
    # Referencias
    pedido_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="ID del Pedido")
    contrato_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="ID del Contrato")
    
    # Configuración de recordatorios
    recordatorio_15min = models.BooleanField(default=False, verbose_name="Recordatorio 15 min antes")
    recordatorio_1hora = models.BooleanField(default=False, verbose_name="Recordatorio 1 hora antes")
    recordatorio_1dia = models.BooleanField(default=False, verbose_name="Recordatorio 1 día antes")
    recordatorio_personalizado = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1)],
        verbose_name="Recordatorio personalizado (minutos antes)"
    )
    
    # Información adicional
    notas_internas = models.TextField(blank=True, verbose_name="Notas Internas")
    material_necesario = models.TextField(blank=True, verbose_name="Material Necesario")
    
    # Repetición (para eventos recurrentes)
    es_recurrente = models.BooleanField(default=False, verbose_name="Es Recurrente")
    patron_recurrencia = models.CharField(max_length=50, blank=True, verbose_name="Patrón de Recurrencia")
    fecha_fin_recurrencia = models.DateField(null=True, blank=True, verbose_name="Fecha Fin de Recurrencia")
    
    class Meta:
        verbose_name = "Evento de Agenda"
        verbose_name_plural = "Eventos de Agenda"
        db_table = "agenda_evento"
        ordering = ['fecha_inicio']
        indexes = [
            models.Index(fields=['tenant_id', 'fecha_inicio']),
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'tipo_evento']),
            models.Index(fields=['tenant_id', 'responsable']),
        ]
    
    def __str__(self):
        return f"{self.titulo} - {self.fecha_inicio.strftime('%d/%m/%Y %H:%M')}"
    
    @property
    def duracion_horas(self):
        """Calcula la duración del evento en horas"""
        if self.fecha_fin and self.fecha_inicio:
            delta = self.fecha_fin - self.fecha_inicio
            return delta.total_seconds() / 3600
        return 0
    
    @property
    def esta_vencido(self):
        """Verifica si el evento ya pasó"""
        from django.utils import timezone
        return self.fecha_fin < timezone.now()


class RecordatorioEnviado(BaseModel):
    """Registro de recordatorios enviados"""
    
    evento = models.ForeignKey(
        EventoAgenda, on_delete=models.CASCADE, related_name='recordatorios_enviados', verbose_name="Evento"
    )
    tipo_recordatorio = models.CharField(max_length=50, verbose_name="Tipo de Recordatorio")
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Envío")
    destinatario = models.CharField(max_length=200, verbose_name="Destinatario")
    metodo_envio = models.CharField(
        max_length=20, choices=[('EMAIL', 'Email'), ('SMS', 'SMS'), ('WHATSAPP', 'WhatsApp')],
        verbose_name="Método de Envío"
    )
    estado_envio = models.CharField(
        max_length=20, choices=[('ENVIADO', 'Enviado'), ('FALLIDO', 'Fallido'), ('PENDIENTE', 'Pendiente')],
        default='PENDIENTE', verbose_name="Estado del Envío"
    )
    mensaje_error = models.TextField(blank=True, verbose_name="Mensaje de Error")
    
    class Meta:
        verbose_name = "Recordatorio Enviado"
        verbose_name_plural = "Recordatorios Enviados"
        db_table = "agenda_recordatorio_enviado"
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.evento.titulo} - {self.tipo_recordatorio} - {self.destinatario}"


class DisponibilidadRecurso(BaseModel):
    """Disponibilidad de recursos para eventos"""
    
    TIPO_RECURSO_CHOICES = [
        ('SALA', 'Sala'),
        ('EQUIPO', 'Equipo'),
        ('VEHICULO', 'Vehículo'),
        ('PERSONAL', 'Personal'),
    ]
    
    nombre_recurso = models.CharField(max_length=100, verbose_name="Nombre del Recurso")
    tipo_recurso = models.CharField(
        max_length=20, choices=TIPO_RECURSO_CHOICES, verbose_name="Tipo de Recurso"
    )
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    capacidad = models.PositiveIntegerField(null=True, blank=True, verbose_name="Capacidad")
    esta_disponible = models.BooleanField(default=True, verbose_name="Está Disponible")
    
    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        db_table = "agenda_recurso"
        ordering = ['tipo_recurso', 'nombre_recurso']
    
    def __str__(self):
        return f"{self.nombre_recurso} ({self.get_tipo_recurso_display()})"


class ReservaRecurso(BaseModel):
    """Reservas de recursos para eventos"""
    
    evento = models.ForeignKey(
        EventoAgenda, on_delete=models.CASCADE, related_name='reservas_recursos', verbose_name="Evento"
    )
    recurso = models.ForeignKey(
        DisponibilidadRecurso, on_delete=models.CASCADE, related_name='reservas', verbose_name="Recurso"
    )
    fecha_inicio_reserva = models.DateTimeField(verbose_name="Inicio de Reserva")
    fecha_fin_reserva = models.DateTimeField(verbose_name="Fin de Reserva")
    cantidad_reservada = models.PositiveIntegerField(default=1, verbose_name="Cantidad Reservada")
    notas = models.TextField(blank=True, verbose_name="Notas")
    
    class Meta:
        verbose_name = "Reserva de Recurso"
        verbose_name_plural = "Reservas de Recursos"
        db_table = "agenda_reserva_recurso"
        ordering = ['fecha_inicio_reserva']
    
    def __str__(self):
        return f"{self.evento.titulo} - {self.recurso.nombre_recurso}"


class HistorialEvento(BaseModel):
    """Historial de cambios en eventos"""
    
    evento = models.ForeignKey(
        EventoAgenda, on_delete=models.CASCADE, related_name='historial', verbose_name="Evento"
    )
    accion = models.CharField(max_length=50, verbose_name="Acción")
    fecha_accion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Acción")
    usuario = models.CharField(max_length=100, verbose_name="Usuario")
    descripcion_cambio = models.TextField(verbose_name="Descripción del Cambio")
    valores_anteriores = models.JSONField(null=True, blank=True, verbose_name="Valores Anteriores")
    valores_nuevos = models.JSONField(null=True, blank=True, verbose_name="Valores Nuevos")
    
    class Meta:
        verbose_name = "Historial de Evento"
        verbose_name_plural = "Historial de Eventos"
        db_table = "agenda_historial_evento"
        ordering = ['-fecha_accion']
    
    def __str__(self):
        return f"{self.evento.titulo} - {self.accion} - {self.fecha_accion.strftime('%d/%m/%Y %H:%M')}"