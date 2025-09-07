from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from apps.core.models import BaseModel


class TipoReporte(models.TextChoices):
    FINANCIERO = 'FINANCIERO', 'Reporte Financiero'
    INVENTARIO = 'INVENTARIO', 'Reporte de Inventario'
    PRODUCCION = 'PRODUCCION', 'Reporte de Producción'
    CLIENTES = 'CLIENTES', 'Reporte de Clientes'
    VENTAS = 'VENTAS', 'Reporte de Ventas'
    PERSONALIZADO = 'PERSONALIZADO', 'Reporte Personalizado'


class EstadoReporte(models.TextChoices):
    PENDIENTE = 'PENDIENTE', 'Pendiente'
    PROCESANDO = 'PROCESANDO', 'Procesando'
    COMPLETADO = 'COMPLETADO', 'Completado'
    ERROR = 'ERROR', 'Error'


class FormatoReporte(models.TextChoices):
    PDF = 'PDF', 'PDF'
    EXCEL = 'EXCEL', 'Excel'
    CSV = 'CSV', 'CSV'
    JSON = 'JSON', 'JSON'


class ReporteGenerado(BaseModel):
    """Reportes generados por el sistema"""
    
    nombre_reporte = models.CharField(max_length=200, verbose_name="Nombre del Reporte")
    tipo_reporte = models.CharField(
        max_length=20, choices=TipoReporte.choices, verbose_name="Tipo de Reporte"
    )
    estado = models.CharField(
        max_length=20, choices=EstadoReporte.choices, default=EstadoReporte.PENDIENTE, verbose_name="Estado"
    )
    formato = models.CharField(
        max_length=10, choices=FormatoReporte.choices, default=FormatoReporte.PDF, verbose_name="Formato"
    )
    
    # Parámetros del reporte
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    parametros_adicionales = models.JSONField(default=dict, blank=True, verbose_name="Parámetros Adicionales")
    
    # Información de generación
    fecha_generacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Generación")
    fecha_completado = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Completado")
    usuario_solicitante = models.CharField(max_length=100, verbose_name="Usuario Solicitante")
    
    # Archivo generado
    archivo_reporte = models.FileField(upload_to='reportes/', null=True, blank=True, verbose_name="Archivo del Reporte")
    tamaño_archivo = models.PositiveIntegerField(null=True, blank=True, verbose_name="Tamaño del Archivo (bytes)")
    
    # Información adicional
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    tiempo_procesamiento = models.DurationField(null=True, blank=True, verbose_name="Tiempo de Procesamiento")
    mensaje_error = models.TextField(blank=True, verbose_name="Mensaje de Error")
    
    # Configuración de eliminación automática
    fecha_expiracion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Expiración")
    auto_eliminar = models.BooleanField(default=True, verbose_name="Auto Eliminar")
    
    class Meta:
        verbose_name = "Reporte Generado"
        verbose_name_plural = "Reportes Generados"
        db_table = "reportes_generado"
        ordering = ['-fecha_generacion']
        indexes = [
            models.Index(fields=['tenant_id', 'tipo_reporte']),
            models.Index(fields=['tenant_id', 'estado']),
            models.Index(fields=['tenant_id', 'fecha_generacion']),
        ]
    
    def __str__(self):
        return f"{self.nombre_reporte} - {self.fecha_generacion.strftime('%d/%m/%Y %H:%M')}"


class MetricaFinanciera(BaseModel):
    """Métricas financieras calculadas"""
    
    PERIODO_CHOICES = [
        ('DIARIO', 'Diario'),
        ('SEMANAL', 'Semanal'),
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    ]
    
    fecha = models.DateField(verbose_name="Fecha")
    periodo = models.CharField(max_length=20, choices=PERIODO_CHOICES, verbose_name="Período")
    
    # Ingresos
    ingresos_impresion = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Ingresos Impresión"
    )
    ingresos_enmarcado = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Ingresos Enmarcado"
    )
    ingresos_recordatorios = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Ingresos Recordatorios"
    )
    ingresos_retoque = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Ingresos Retoque"
    )
    ingresos_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Ingresos Total"
    )
    
    # Costos
    costos_materiales = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Costos de Materiales"
    )
    costos_operativos = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Costos Operativos"
    )
    costos_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Costos Total"
    )
    
    # Utilidades
    utilidad_bruta = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Utilidad Bruta"
    )
    margen_utilidad = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal('0.00'), verbose_name="Margen de Utilidad (%)"
    )
    
    # Cantidades
    cantidad_pedidos = models.PositiveIntegerField(default=0, verbose_name="Cantidad de Pedidos")
    cantidad_clientes_nuevos = models.PositiveIntegerField(default=0, verbose_name="Clientes Nuevos")
    
    class Meta:
        verbose_name = "Métrica Financiera"
        verbose_name_plural = "Métricas Financieras"
        db_table = "reportes_metrica_financiera"
        ordering = ['-fecha']
        unique_together = ('tenant_id', 'fecha', 'periodo')
    
    def __str__(self):
        return f"Métricas {self.get_periodo_display()} - {self.fecha}"


class MetricaInventario(BaseModel):
    """Métricas de inventario"""
    
    fecha = models.DateField(verbose_name="Fecha")
    
    # Varillas
    varillas_stock_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Stock Total Varillas"
    )
    varillas_stock_bajo = models.PositiveIntegerField(default=0, verbose_name="Varillas con Stock Bajo")
    varillas_agotadas = models.PositiveIntegerField(default=0, verbose_name="Varillas Agotadas")
    
    # Materiales de impresión
    materiales_impresion_total = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Total Materiales Impresión"
    )
    materiales_impresion_stock_bajo = models.PositiveIntegerField(default=0, verbose_name="Materiales Impresión Stock Bajo")
    
    # Productos terminados
    productos_terminados_total = models.PositiveIntegerField(default=0, verbose_name="Total Productos Terminados")
    productos_en_almacen = models.PositiveIntegerField(default=0, verbose_name="Productos en Almacén")
    productos_en_tienda = models.PositiveIntegerField(default=0, verbose_name="Productos en Tienda")
    
    # Movimientos
    movimientos_entrada = models.PositiveIntegerField(default=0, verbose_name="Movimientos de Entrada")
    movimientos_salida = models.PositiveIntegerField(default=0, verbose_name="Movimientos de Salida")
    
    # Valor del inventario
    valor_total_inventario = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal('0.00'), verbose_name="Valor Total del Inventario"
    )
    
    class Meta:
        verbose_name = "Métrica de Inventario"
        verbose_name_plural = "Métricas de Inventario"
        db_table = "reportes_metrica_inventario"
        ordering = ['-fecha']
        unique_together = ('tenant_id', 'fecha')
    
    def __str__(self):
        return f"Inventario - {self.fecha}"


class MetricaProduccion(BaseModel):
    """Métricas de producción"""
    
    fecha = models.DateField(verbose_name="Fecha")
    
    # Órdenes de producción
    ordenes_abiertas = models.PositiveIntegerField(default=0, verbose_name="Órdenes Abiertas")
    ordenes_en_proceso = models.PositiveIntegerField(default=0, verbose_name="Órdenes en Proceso")
    ordenes_cerradas = models.PositiveIntegerField(default=0, verbose_name="Órdenes Cerradas")
    ordenes_canceladas = models.PositiveIntegerField(default=0, verbose_name="Órdenes Canceladas")
    
    # Producción
    cuadros_producidos = models.PositiveIntegerField(default=0, verbose_name="Cuadros Producidos")
    tiempo_promedio_produccion = models.DurationField(null=True, blank=True, verbose_name="Tiempo Promedio de Producción")
    
    # Eficiencia
    porcentaje_merma = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal('0.00'), verbose_name="Porcentaje de Merma"
    )
    eficiencia_produccion = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal('0.00'), verbose_name="Eficiencia de Producción (%)"
    )
    
    # Control de calidad
    productos_aprobados = models.PositiveIntegerField(default=0, verbose_name="Productos Aprobados")
    productos_rechazados = models.PositiveIntegerField(default=0, verbose_name="Productos Rechazados")
    productos_requieren_reparacion = models.PositiveIntegerField(default=0, verbose_name="Productos que Requieren Reparación")
    
    class Meta:
        verbose_name = "Métrica de Producción"
        verbose_name_plural = "Métricas de Producción"
        db_table = "reportes_metrica_produccion"
        ordering = ['-fecha']
        unique_together = ('tenant_id', 'fecha')
    
    def __str__(self):
        return f"Producción - {self.fecha}"


class ConfiguracionReporte(BaseModel):
    """Configuraciones predefinidas para reportes"""
    
    nombre_configuracion = models.CharField(max_length=100, verbose_name="Nombre de la Configuración")
    tipo_reporte = models.CharField(
        max_length=20, choices=TipoReporte.choices, verbose_name="Tipo de Reporte"
    )
    parametros = models.JSONField(default=dict, verbose_name="Parámetros")
    formato_predeterminado = models.CharField(
        max_length=10, choices=FormatoReporte.choices, default=FormatoReporte.PDF, verbose_name="Formato Predeterminado"
    )
    es_publico = models.BooleanField(default=False, verbose_name="Es Público")
    creado_por = models.CharField(max_length=100, verbose_name="Creado por")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    
    class Meta:
        verbose_name = "Configuración de Reporte"
        verbose_name_plural = "Configuraciones de Reportes"
        db_table = "reportes_configuracion"
        ordering = ['nombre_configuracion']
    
    def __str__(self):
        return self.nombre_configuracion