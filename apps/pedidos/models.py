from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel
from apps.clientes.models import Cliente


class TipoServicio(models.TextChoices):
    IMPRESION = 'IMPRESION', 'Impresión Minilab'
    ENMARCADO = 'ENMARCADO', 'Enmarcado'
    RECORDATORIO = 'RECORDATORIO', 'Recordatorio Escolar'
    RETOQUE = 'RETOQUE', 'Retoque Fotográfico'


class EstadoPedido(models.TextChoices):
    NUEVO = 'NUEVO', 'Nuevo'
    PRODUCCION = 'PRODUCCION', 'En Producción'
    ENTREGADO = 'ENTREGADO', 'Entregado'
    CANCELADO = 'CANCELADO', 'Cancelado'


class Prioridad(models.TextChoices):
    BAJA = 'BAJA', 'Baja'
    MEDIA = 'MEDIA', 'Media'
    ALTA = 'ALTA', 'Alta'


class Pedido(BaseModel):
    """Modelo principal para gestionar pedidos"""
    
    # Información básica
    numero_pedido = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Número de Pedido"
    )
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.PROTECT, 
        related_name='pedidos',
        verbose_name="Cliente"
    )
    tipo_servicio = models.CharField(
        max_length=20, 
        choices=TipoServicio.choices,
        verbose_name="Tipo de Servicio"
    )
    estado = models.CharField(
        max_length=20, 
        choices=EstadoPedido.choices, 
        default=EstadoPedido.NUEVO,
        verbose_name="Estado"
    )
    prioridad = models.CharField(
        max_length=10, 
        choices=Prioridad.choices, 
        default=Prioridad.MEDIA,
        verbose_name="Prioridad"
    )
    
    # Fechas
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Pedido")
    fecha_entrega_estimada = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Entrega Estimada")
    fecha_entrega_real = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Entrega Real")
    
    # Información adicional
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    
    # Campos financieros
    monto_total = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Monto Total"
    )
    monto_adelanto = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Monto de Adelanto"
    )
    
    # Usuario que creó el pedido
    creado_por = models.CharField(max_length=100, verbose_name="Creado por")
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        db_table = "pedidos_pedido"
        ordering = ['-fecha_pedido']
        indexes = [
            models.Index(fields=['tenant_id', 'numero_pedido']),
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'tipo_servicio']),
            models.Index(fields=['tenant_id', 'fecha_pedido']),
        ]
    
    def __str__(self):
        return f"{self.numero_pedido} - {self.cliente}"
    
    @property
    def monto_pendiente(self):
        """Calcula el monto pendiente de pago"""
        return self.monto_total - self.monto_adelanto
    
    @property
    def porcentaje_adelanto(self):
        """Calcula el porcentaje de adelanto"""
        if self.monto_total > 0:
            return (self.monto_adelanto / self.monto_total) * 100
        return 0
    
    def save(self, *args, **kwargs):
        if not self.numero_pedido:
            # Generar número de pedido automáticamente
            import datetime
            now = datetime.datetime.now()
            self.numero_pedido = f"P{now.strftime('%Y%m%d')}{now.strftime('%H%M%S')}"
        super().save(*args, **kwargs)


class DetallePedidoImpresion(BaseModel):
    """Detalles específicos para pedidos de impresión"""
    
    TIPO_PAPEL_CHOICES = [
        ('10x15', '10x15 cm'),
        ('13x18', '13x18 cm'),
        ('15x21', '15x21 cm'),
        ('20x25', '20x25 cm'),
    ]
    
    pedido = models.OneToOneField(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='detalle_impresion',
        verbose_name="Pedido"
    )
    tipo_papel = models.CharField(
        max_length=10, 
        choices=TIPO_PAPEL_CHOICES,
        verbose_name="Tipo de Papel"
    )
    cantidad_fotos = models.PositiveIntegerField(verbose_name="Cantidad de Fotos")
    acabado = models.CharField(max_length=50, blank=True, verbose_name="Acabado")
    tiempo_estimado_horas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Tiempo Estimado (horas)")
    
    class Meta:
        verbose_name = "Detalle de Impresión"
        verbose_name_plural = "Detalles de Impresión"
        db_table = "pedidos_detalle_impresion"
    
    def __str__(self):
        return f"Impresión - {self.pedido.numero_pedido}"


class DetallePedidoEnmarcado(BaseModel):
    """Detalles específicos para pedidos de enmarcado"""
    
    TIPO_MARCO_CHOICES = [
        ('ARTESANAL', 'Artesanal (a medida)'),
        ('ESTANDAR', 'Estándar (preensamblado)'),
    ]
    
    pedido = models.OneToOneField(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='detalle_enmarcado',
        verbose_name="Pedido"
    )
    tipo_marco = models.CharField(
        max_length=20, 
        choices=TIPO_MARCO_CHOICES,
        verbose_name="Tipo de Marco"
    )
    ancho_cm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name="Ancho (cm)"
    )
    alto_cm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name="Alto (cm)"
    )
    color_marco = models.CharField(max_length=50, blank=True, verbose_name="Color del Marco")
    material_marco = models.CharField(max_length=50, blank=True, verbose_name="Material del Marco")
    incluye_vidrio = models.BooleanField(default=True, verbose_name="Incluye Vidrio")
    tiempo_estimado_horas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Tiempo Estimado (horas)")
    
    class Meta:
        verbose_name = "Detalle de Enmarcado"
        verbose_name_plural = "Detalles de Enmarcado"
        db_table = "pedidos_detalle_enmarcado"
    
    def __str__(self):
        return f"Enmarcado - {self.pedido.numero_pedido}"


class DetallePedidoRecordatorio(BaseModel):
    """Detalles específicos para pedidos de recordatorios escolares"""
    
    pedido = models.OneToOneField(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='detalle_recordatorio',
        verbose_name="Pedido"
    )
    plantilla_id = models.CharField(max_length=50, verbose_name="ID de Plantilla")
    nombre_plantilla = models.CharField(max_length=100, verbose_name="Nombre de la Plantilla")
    cantidad_recordatorios = models.PositiveIntegerField(verbose_name="Cantidad de Recordatorios")
    grado_seccion = models.CharField(max_length=50, blank=True, verbose_name="Grado y Sección")
    año_escolar = models.CharField(max_length=10, blank=True, verbose_name="Año Escolar")
    tiempo_estimado_horas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Tiempo Estimado (horas)")
    
    class Meta:
        verbose_name = "Detalle de Recordatorio"
        verbose_name_plural = "Detalles de Recordatorio"
        db_table = "pedidos_detalle_recordatorio"
    
    def __str__(self):
        return f"Recordatorio - {self.pedido.numero_pedido}"


class DetallePedidoRetoque(BaseModel):
    """Detalles específicos para pedidos de retoque fotográfico"""
    
    TIPO_RETOQUE_CHOICES = [
        ('RESTAURACION', 'Restauración'),
        ('RETOQUE', 'Retoque Digital'),
        ('COLORIZACION', 'Colorización'),
    ]
    
    pedido = models.OneToOneField(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='detalle_retoque',
        verbose_name="Pedido"
    )
    tipo_retoque = models.CharField(
        max_length=20, 
        choices=TIPO_RETOQUE_CHOICES,
        verbose_name="Tipo de Retoque"
    )
    descripcion_trabajo = models.TextField(verbose_name="Descripción del Trabajo")
    cantidad_fotos = models.PositiveIntegerField(verbose_name="Cantidad de Fotos")
    tiempo_estimado_horas = models.PositiveIntegerField(null=True, blank=True, verbose_name="Tiempo Estimado (horas)")
    
    class Meta:
        verbose_name = "Detalle de Retoque"
        verbose_name_plural = "Detalles de Retoque"
        db_table = "pedidos_detalle_retoque"
    
    def __str__(self):
        return f"Retoque - {self.pedido.numero_pedido}"


class ArchivoPedido(BaseModel):
    """Archivos asociados a los pedidos"""
    
    pedido = models.ForeignKey(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='archivos',
        verbose_name="Pedido"
    )
    archivo = models.FileField(upload_to='pedidos/archivos/', verbose_name="Archivo")
    nombre_original = models.CharField(max_length=255, verbose_name="Nombre Original")
    descripcion = models.CharField(max_length=200, blank=True, verbose_name="Descripción")
    tamaño = models.PositiveIntegerField(verbose_name="Tamaño en bytes")
    tipo_mime = models.CharField(max_length=100, verbose_name="Tipo MIME")
    
    class Meta:
        verbose_name = "Archivo de Pedido"
        verbose_name_plural = "Archivos de Pedidos"
        db_table = "pedidos_archivo"
        ordering = ['nombre_original']
    
    def __str__(self):
        return f"{self.nombre_original} - {self.pedido.numero_pedido}"


class HistorialEstadoPedido(BaseModel):
    """Historial de cambios de estado de los pedidos"""
    
    pedido = models.ForeignKey(
        Pedido, 
        on_delete=models.CASCADE, 
        related_name='historial_estados',
        verbose_name="Pedido"
    )
    estado_anterior = models.CharField(
        max_length=20, 
        choices=EstadoPedido.choices,
        null=True, 
        blank=True,
        verbose_name="Estado Anterior"
    )
    estado_nuevo = models.CharField(
        max_length=20, 
        choices=EstadoPedido.choices,
        verbose_name="Estado Nuevo"
    )
    fecha_cambio = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Cambio")
    usuario = models.CharField(max_length=100, verbose_name="Usuario")
    comentarios = models.TextField(blank=True, verbose_name="Comentarios")
    
    class Meta:
        verbose_name = "Historial de Estado"
        verbose_name_plural = "Historial de Estados"
        db_table = "pedidos_historial_estado"
        ordering = ['-fecha_cambio']
    
    def __str__(self):
        return f"{self.pedido.numero_pedido} - {self.estado_anterior} → {self.estado_nuevo}"