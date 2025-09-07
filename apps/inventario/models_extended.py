from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel
from .models import UnidadMedida


class PinturaAcabado(BaseModel):
    """Pinturas y acabados para marcos"""
    
    TIPO_CHOICES = [
        ('PINTURA', 'Pintura'),
        ('BARNIZ', 'Barniz'),
        ('LACA', 'Laca'),
        ('TINTE', 'Tinte'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo")
    color = models.CharField(max_length=50, verbose_name="Color")
    marca = models.CharField(max_length=50, blank=True, verbose_name="Marca")
    
    # Inventario
    stock_actual = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Actual"
    )
    stock_minimo = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Mínimo"
    )
    unidad_medida = models.CharField(
        max_length=20, choices=UnidadMedida.choices,
        default=UnidadMedida.LITRO, verbose_name="Unidad de Medida"
    )
    
    # Precios
    precio_compra = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Compra"
    )
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Venta"
    )
    
    class Meta:
        verbose_name = "Pintura/Acabado"
        verbose_name_plural = "Pinturas/Acabados"
        db_table = "inventario_pintura_acabado"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class MaterialImpresion(BaseModel):
    """Materiales para impresión fotográfica"""
    
    TIPO_CHOICES = [
        ('PAPEL', 'Papel Fotográfico'),
        ('QUIMICO', 'Químico'),
        ('TINTA', 'Tinta'),
        ('CONSUMIBLE', 'Consumible'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo")
    marca = models.CharField(max_length=50, blank=True, verbose_name="Marca")
    
    # Para papel fotográfico
    tamaño = models.CharField(max_length=20, blank=True, verbose_name="Tamaño")
    acabado = models.CharField(max_length=50, blank=True, verbose_name="Acabado")
    
    # Inventario
    stock_actual = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Actual"
    )
    stock_minimo = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Mínimo"
    )
    unidad_medida = models.CharField(
        max_length=20, choices=UnidadMedida.choices,
        default=UnidadMedida.UNIDAD, verbose_name="Unidad de Medida"
    )
    
    # Precios
    precio_compra = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Compra"
    )
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Venta"
    )
    
    class Meta:
        verbose_name = "Material de Impresión"
        verbose_name_plural = "Materiales de Impresión"
        db_table = "inventario_material_impresion"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class MaterialRecordatorio(BaseModel):
    """Materiales para recordatorios escolares"""
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    
    # Inventario
    stock_actual = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Actual"
    )
    stock_minimo = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))], verbose_name="Stock Mínimo"
    )
    unidad_medida = models.CharField(
        max_length=20, choices=UnidadMedida.choices,
        default=UnidadMedida.UNIDAD, verbose_name="Unidad de Medida"
    )
    
    # Precios
    precio_compra = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Compra"
    )
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Venta"
    )
    
    class Meta:
        verbose_name = "Material de Recordatorio"
        verbose_name_plural = "Materiales de Recordatorio"
        db_table = "inventario_material_recordatorio"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class MovimientoInventario(BaseModel):
    """Historial de movimientos de inventario"""
    
    TIPO_MOVIMIENTO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
        ('AJUSTE', 'Ajuste'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]
    
    MOTIVO_CHOICES = [
        ('COMPRA', 'Compra'),
        ('VENTA', 'Venta'),
        ('PRODUCCION', 'Uso en Producción'),
        ('DEVOLUCION', 'Devolución'),
        ('MERMA', 'Merma'),
        ('AJUSTE_INVENTARIO', 'Ajuste de Inventario'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]
    
    # Referencia al material
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.CharField(max_length=36)
    
    # Detalles del movimiento
    tipo_movimiento = models.CharField(
        max_length=20, choices=TIPO_MOVIMIENTO_CHOICES, verbose_name="Tipo de Movimiento"
    )
    motivo = models.CharField(max_length=30, choices=MOTIVO_CHOICES, verbose_name="Motivo")
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cantidad")
    unidad_medida = models.CharField(
        max_length=20, choices=UnidadMedida.choices, verbose_name="Unidad de Medida"
    )
    
    # Stock antes y después del movimiento
    stock_anterior = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Stock Anterior")
    stock_nuevo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Stock Nuevo")
    
    # Información adicional
    fecha_movimiento = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Movimiento")
    usuario = models.CharField(max_length=100, verbose_name="Usuario")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    documento_referencia = models.CharField(max_length=100, blank=True, verbose_name="Documento de Referencia")
    
    # Costos
    costo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Costo Unitario"
    )
    costo_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Costo Total"
    )
    
    class Meta:
        verbose_name = "Movimiento de Inventario"
        verbose_name_plural = "Movimientos de Inventario"
        db_table = "inventario_movimiento"
        ordering = ['-fecha_movimiento']
        indexes = [
            models.Index(fields=['tenant_id', 'fecha_movimiento']),
            models.Index(fields=['tenant_id', 'tipo_movimiento']),
        ]
    
    def __str__(self):
        return f"{self.tipo_movimiento} - {self.cantidad} - {self.fecha_movimiento.strftime('%d/%m/%Y')}"


class ProductoTerminado(BaseModel):
    """Productos terminados listos para venta/entrega"""
    
    ESTADO_CHOICES = [
        ('EN_ALMACEN', 'En Almacén'),
        ('EN_TIENDA', 'En Tienda'),
        ('VENDIDO', 'Vendido'),
        ('ENTREGADO', 'Entregado'),
        ('DEFECTUOSO', 'Defectuoso'),
    ]
    
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción")
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='EN_ALMACEN', verbose_name="Estado"
    )
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación")
    
    # Referencias
    pedido_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="ID del Pedido")
    orden_produccion_id = models.CharField(max_length=36, null=True, blank=True, verbose_name="ID de Orden de Producción")
    
    # Fechas
    fecha_produccion = models.DateTimeField(verbose_name="Fecha de Producción")
    fecha_venta = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Venta")
    fecha_entrega = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Entrega")
    
    # Información financiera
    costo_produccion = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Costo de Producción"
    )
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Venta"
    )
    
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    
    class Meta:
        verbose_name = "Producto Terminado"
        verbose_name_plural = "Productos Terminados"
        db_table = "inventario_producto_terminado"
        ordering = ['-fecha_produccion']
        indexes = [
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'codigo']),
        ]
    
    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
