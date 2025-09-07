from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel


class EstadoOrden(models.TextChoices):
    ABIERTA = 'ABIERTA', 'Abierta'
    EN_PROCESO = 'EN_PROCESO', 'En Proceso'
    CERRADA = 'CERRADA', 'Cerrada'
    CANCELADA = 'CANCELADA', 'Cancelada'


class EstadoCuadro(models.TextChoices):
    EN_PRODUCCION = 'EN_PRODUCCION', 'En Producción'
    EN_ALMACEN = 'EN_ALMACEN', 'En Almacén'
    EN_TIENDA = 'EN_TIENDA', 'En Tienda'
    VENDIDO = 'VENDIDO', 'Vendido'


class OrdenProduccion(BaseModel):
    """Órdenes de producción para marcos y cuadros"""
    
    numero_orden = models.CharField(max_length=20, unique=True, verbose_name="Número de Orden")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    solicitado_por = models.CharField(max_length=100, verbose_name="Solicitado por")
    responsable_produccion = models.CharField(max_length=100, verbose_name="Responsable de Producción")
    
    estado = models.CharField(
        max_length=20, choices=EstadoOrden.choices, default=EstadoOrden.ABIERTA, verbose_name="Estado"
    )
    
    # Fechas importantes
    fecha_inicio_programada = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Inicio Programada")
    fecha_fin_programada = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Fin Programada")
    fecha_inicio_real = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Inicio Real")
    fecha_fin_real = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Fin Real")
    
    # Información adicional
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    prioridad = models.CharField(
        max_length=10, choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta')],
        default='MEDIA', verbose_name="Prioridad"
    )
    
    # Referencia al pedido si existe
    pedido_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="ID del Pedido")
    
    class Meta:
        verbose_name = "Orden de Producción"
        verbose_name_plural = "Órdenes de Producción"
        db_table = "produccion_orden"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['tenant_id', 'numero_orden']),
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'fecha_creacion']),
        ]
    
    def __str__(self):
        return f"{self.numero_orden} - {self.solicitado_por}"
    
    def save(self, *args, **kwargs):
        if not self.numero_orden:
            import datetime
            now = datetime.datetime.now()
            self.numero_orden = f"OP{now.strftime('%Y%m%d')}{now.strftime('%H%M%S')}"
        super().save(*args, **kwargs)


class Cuadro(BaseModel):
    """Cuadros producidos y su estado en el sistema"""
    
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código del Cuadro")
    nombre = models.CharField(max_length=200, verbose_name="Nombre/Descripción")
    
    # Dimensiones
    alto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Alto (cm)")
    ancho = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Ancho (cm)")
    profundidad = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('3.00'), verbose_name="Profundidad (cm)")
    
    # Estado y ubicación
    estado = models.CharField(
        max_length=20, choices=EstadoCuadro.choices, default=EstadoCuadro.EN_PRODUCCION, verbose_name="Estado"
    )
    
    # Relación con orden de producción
    orden_produccion = models.ForeignKey(
        OrdenProduccion, on_delete=models.CASCADE, related_name='cuadros', verbose_name="Orden de Producción"
    )
    
    # Información de costos
    costo_materiales = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'), 
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Costo de Materiales"
    )
    costo_mano_obra = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Costo de Mano de Obra"
    )
    
    # Fechas
    fecha_inicio_produccion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Inicio de Producción")
    fecha_fin_produccion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Fin de Producción")
    
    # Información adicional
    notas = models.TextField(blank=True, verbose_name="Notas")
    imagen = models.ImageField(upload_to='cuadros/', null=True, blank=True, verbose_name="Imagen")
    
    class Meta:
        verbose_name = "Cuadro"
        verbose_name_plural = "Cuadros"
        db_table = "produccion_cuadro"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['tenant_id', 'codigo']),
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'orden_produccion']),
        ]
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    @property
    def costo_total(self):
        return self.costo_materiales + self.costo_mano_obra
    
    @property
    def area(self):
        return self.alto * self.ancho / 10000  # Resultado en m²
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            import datetime
            now = datetime.datetime.now()
            self.codigo = f"CU{now.strftime('%Y%m%d')}{now.strftime('%H%M%S')}"
        super().save(*args, **kwargs)