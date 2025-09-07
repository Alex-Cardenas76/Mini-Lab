from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel


class UnidadMedida(models.TextChoices):
    UNIDAD = 'UNIDAD', 'Unidad'
    METRO = 'METRO', 'Metro'
    LITRO = 'LITRO', 'Litro'
    KILOGRAMO = 'KILOGRAMO', 'Kilogramo'
    ROLLO = 'ROLLO', 'Rollo'
    CAJA = 'CAJA', 'Caja'


class EstadoInventario(models.TextChoices):
    DISPONIBLE = 'DISPONIBLE', 'Disponible'
    AGOTADO = 'AGOTADO', 'Agotado'
    STOCK_BAJO = 'STOCK_BAJO', 'Stock Bajo'
    DESCONTINUADO = 'DESCONTINUADO', 'Descontinuado'


class CategoriaInventario(BaseModel):
    """Categorías para organizar el inventario"""
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    
    class Meta:
        verbose_name = "Categoría de Inventario"
        verbose_name_plural = "Categorías de Inventario"
        db_table = "inventario_categoria"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Varilla(BaseModel):
    """Varillas/Molduras para enmarcado"""
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    categoria = models.ForeignKey(
        CategoriaInventario, 
        on_delete=models.PROTECT,
        related_name='varillas',
        verbose_name="Categoría"
    )
    
    # Características físicas
    material = models.CharField(max_length=50, verbose_name="Material")
    color = models.CharField(max_length=50, verbose_name="Color")
    ancho_mm = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ancho (mm)")
    alto_mm = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Alto (mm)")
    
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
        default=UnidadMedida.METRO, verbose_name="Unidad de Medida"
    )
    
    # Precios
    precio_compra = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Compra"
    )
    precio_venta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Venta"
    )
    
    proveedor = models.CharField(max_length=200, blank=True, verbose_name="Proveedor")
    
    class Meta:
        verbose_name = "Varilla"
        verbose_name_plural = "Varillas"
        db_table = "inventario_varilla"
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['tenant_id', 'codigo']),
            models.Index(fields=['tenant_id', 'categoria']),
        ]
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    @property
    def estado_stock(self):
        """Determina el estado del stock"""
        if self.stock_actual <= 0:
            return EstadoInventario.AGOTADO
        elif self.stock_actual <= self.stock_minimo:
            return EstadoInventario.STOCK_BAJO
        else:
            return EstadoInventario.DISPONIBLE