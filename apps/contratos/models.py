from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel
from apps.clientes.models import Cliente


class EstadoContrato(models.TextChoices):
    BORRADOR = 'BORRADOR', 'Borrador'
    ACTIVO = 'ACTIVO', 'Activo'
    VENCIDO = 'VENCIDO', 'Vencido'
    RENOVADO = 'RENOVADO', 'Renovado'
    CANCELADO = 'CANCELADO', 'Cancelado'


class TipoContrato(models.TextChoices):
    ESCOLAR = 'ESCOLAR', 'Contrato Escolar'
    EMPRESARIAL = 'EMPRESARIAL', 'Contrato Empresarial'
    EVENTO = 'EVENTO', 'Contrato de Evento'


class Contrato(BaseModel):
    """Contratos con clientes corporativos"""
    
    numero_contrato = models.CharField(max_length=20, unique=True, verbose_name="Número de Contrato")
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name='contratos', verbose_name="Cliente"
    )
    tipo_contrato = models.CharField(
        max_length=20, choices=TipoContrato.choices, verbose_name="Tipo de Contrato"
    )
    estado = models.CharField(
        max_length=20, choices=EstadoContrato.choices, default=EstadoContrato.BORRADOR, verbose_name="Estado"
    )
    
    # Fechas del contrato
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    fecha_firma = models.DateField(null=True, blank=True, verbose_name="Fecha de Firma")
    
    # Información del servicio
    descripcion_servicio = models.TextField(verbose_name="Descripción del Servicio")
    alcance = models.TextField(blank=True, verbose_name="Alcance")
    
    # Información financiera
    monto_total = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Monto Total"
    )
    forma_pago = models.CharField(max_length=100, blank=True, verbose_name="Forma de Pago")
    
    # Términos y condiciones
    terminos_condiciones = models.TextField(blank=True, verbose_name="Términos y Condiciones")
    clausulas_especiales = models.TextField(blank=True, verbose_name="Cláusulas Especiales")
    
    # Información de renovación
    renovacion_automatica = models.BooleanField(default=False, verbose_name="Renovación Automática")
    periodo_renovacion_meses = models.PositiveIntegerField(null=True, blank=True, verbose_name="Período de Renovación (meses)")
    
    # Responsables
    responsable_empresa = models.CharField(max_length=100, verbose_name="Responsable de la Empresa")
    responsable_cliente = models.CharField(max_length=100, blank=True, verbose_name="Responsable del Cliente")
    
    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        db_table = "contratos_contrato"
        ordering = ['-fecha_inicio']
        indexes = [
            models.Index(fields=['tenant_id', 'numero_contrato']),
            models.Index(fields=['tenant_id', 'cliente']),
            models.Index(fields=['tenant_id', 'estado']),
        ]
    
    def __str__(self):
        return f"{self.numero_contrato} - {self.cliente}"
    
    def save(self, *args, **kwargs):
        if not self.numero_contrato:
            import datetime
            now = datetime.datetime.now()
            self.numero_contrato = f"CT{now.strftime('%Y%m%d')}{now.strftime('%H%M%S')}"
        super().save(*args, **kwargs)
    
    @property
    def dias_vigencia(self):
        """Calcula los días de vigencia del contrato"""
        return (self.fecha_fin - self.fecha_inicio).days
    
    @property
    def esta_vigente(self):
        """Verifica si el contrato está vigente"""
        from django.utils import timezone
        today = timezone.now().date()
        return self.fecha_inicio <= today <= self.fecha_fin and self.estado == EstadoContrato.ACTIVO


class ContratoEscolar(BaseModel):
    """Detalles específicos para contratos escolares"""
    
    contrato = models.OneToOneField(
        Contrato, on_delete=models.CASCADE, related_name='detalle_escolar', verbose_name="Contrato"
    )
    
    # Información del colegio
    año_escolar = models.CharField(max_length=10, verbose_name="Año Escolar")
    cantidad_alumnos = models.PositiveIntegerField(verbose_name="Cantidad de Alumnos")
    grados_incluidos = models.CharField(max_length=200, verbose_name="Grados Incluidos")
    
    # Servicios incluidos
    incluye_foto_individual = models.BooleanField(default=True, verbose_name="Incluye Foto Individual")
    incluye_foto_grupal = models.BooleanField(default=False, verbose_name="Incluye Foto Grupal")
    incluye_recordatorios = models.BooleanField(default=True, verbose_name="Incluye Recordatorios")
    cantidad_recordatorios_por_alumno = models.PositiveIntegerField(default=1, verbose_name="Recordatorios por Alumno")
    
    # Fechas específicas
    fecha_sesion_fotos = models.DateField(null=True, blank=True, verbose_name="Fecha de Sesión de Fotos")
    fecha_entrega_recordatorios = models.DateField(null=True, blank=True, verbose_name="Fecha de Entrega de Recordatorios")
    
    # Plantillas y diseños
    plantilla_recordatorio = models.CharField(max_length=100, blank=True, verbose_name="Plantilla de Recordatorio")
    diseño_personalizado = models.BooleanField(default=False, verbose_name="Diseño Personalizado")
    
    class Meta:
        verbose_name = "Contrato Escolar"
        verbose_name_plural = "Contratos Escolares"
        db_table = "contratos_escolar"
    
    def __str__(self):
        return f"Escolar - {self.contrato.numero_contrato}"


class PagoContrato(BaseModel):
    """Pagos realizados para los contratos"""
    
    contrato = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, related_name='pagos', verbose_name="Contrato"
    )
    numero_pago = models.CharField(max_length=20, verbose_name="Número de Pago")
    fecha_pago = models.DateField(verbose_name="Fecha de Pago")
    monto = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Monto"
    )
    metodo_pago = models.CharField(max_length=50, verbose_name="Método de Pago")
    referencia = models.CharField(max_length=100, blank=True, verbose_name="Referencia")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    
    # Información del recibo
    numero_recibo = models.CharField(max_length=20, blank=True, verbose_name="Número de Recibo")
    archivo_recibo = models.FileField(upload_to='contratos/recibos/', null=True, blank=True, verbose_name="Archivo del Recibo")
    
    class Meta:
        verbose_name = "Pago de Contrato"
        verbose_name_plural = "Pagos de Contratos"
        db_table = "contratos_pago"
        ordering = ['-fecha_pago']
        unique_together = ('contrato', 'numero_pago')
    
    def __str__(self):
        return f"{self.contrato.numero_contrato} - Pago {self.numero_pago}"


class RenovacionContrato(BaseModel):
    """Historial de renovaciones de contratos"""
    
    contrato_original = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, related_name='renovaciones', verbose_name="Contrato Original"
    )
    contrato_renovado = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, related_name='renovacion_de', null=True, blank=True, verbose_name="Contrato Renovado"
    )
    fecha_renovacion = models.DateField(verbose_name="Fecha de Renovación")
    motivo_renovacion = models.TextField(blank=True, verbose_name="Motivo de Renovación")
    cambios_realizados = models.TextField(blank=True, verbose_name="Cambios Realizados")
    
    class Meta:
        verbose_name = "Renovación de Contrato"
        verbose_name_plural = "Renovaciones de Contratos"
        db_table = "contratos_renovacion"
        ordering = ['-fecha_renovacion']
    
    def __str__(self):
        return f"Renovación {self.contrato_original.numero_contrato}"


class DocumentoContrato(BaseModel):
    """Documentos asociados a los contratos"""
    
    TIPO_DOCUMENTO_CHOICES = [
        ('CONTRATO', 'Contrato'),
        ('ANEXO', 'Anexo'),
        ('ADDENDUM', 'Addendum'),
        ('RECIBO', 'Recibo'),
        ('OTRO', 'Otro'),
    ]
    
    contrato = models.ForeignKey(
        Contrato, on_delete=models.CASCADE, related_name='documentos', verbose_name="Contrato"
    )
    tipo_documento = models.CharField(
        max_length=20, choices=TIPO_DOCUMENTO_CHOICES, verbose_name="Tipo de Documento"
    )
    nombre_documento = models.CharField(max_length=200, verbose_name="Nombre del Documento")
    archivo = models.FileField(upload_to='contratos/documentos/', verbose_name="Archivo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    fecha_subida = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Subida")
    
    class Meta:
        verbose_name = "Documento de Contrato"
        verbose_name_plural = "Documentos de Contratos"
        db_table = "contratos_documento"
        ordering = ['-fecha_subida']
    
    def __str__(self):
        return f"{self.contrato.numero_contrato} - {self.nombre_documento}"