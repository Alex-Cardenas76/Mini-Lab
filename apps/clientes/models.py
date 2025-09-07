from django.db import models
from apps.core.models import BaseModel


class TipoCliente(models.TextChoices):
    PARTICULAR = 'PARTICULAR', 'Cliente Particular'
    COLEGIO = 'COLEGIO', 'Colegio/Institución'
    EMPRESA = 'EMPRESA', 'Empresa'


class Cliente(BaseModel):
    """Modelo para gestionar clientes particulares y corporativos"""
    
    # Información básica
    tipo = models.CharField(
        max_length=20, 
        choices=TipoCliente.choices, 
        default=TipoCliente.PARTICULAR,
        verbose_name="Tipo de Cliente"
    )
    
    # Para clientes particulares
    nombres = models.CharField(max_length=100, blank=True, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, blank=True, verbose_name="Apellidos")
    
    # Para clientes corporativos (colegios/empresas)
    razon_social = models.CharField(max_length=200, blank=True, verbose_name="Razón Social")
    nombre_comercial = models.CharField(max_length=200, blank=True, verbose_name="Nombre Comercial")
    ruc = models.CharField(max_length=11, blank=True, verbose_name="RUC")
    
    # Información de contacto
    dni = models.CharField(max_length=8, blank=True, verbose_name="DNI")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    email = models.EmailField(blank=True, verbose_name="Email")
    direccion = models.TextField(blank=True, verbose_name="Dirección")
    
    # Información adicional
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    
    # Para colegios específicamente
    director = models.CharField(max_length=150, blank=True, verbose_name="Director")
    nivel_educativo = models.CharField(max_length=50, blank=True, verbose_name="Nivel Educativo")
    cantidad_alumnos = models.PositiveIntegerField(null=True, blank=True, verbose_name="Cantidad de Alumnos")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "clientes_cliente"
        ordering = ['tipo', 'razon_social', 'apellidos', 'nombres']
        indexes = [
            models.Index(fields=['tenant_id', 'tipo']),
            models.Index(fields=['tenant_id', 'dni']),
            models.Index(fields=['tenant_id', 'ruc']),
        ]
    
    def __str__(self):
        if self.tipo == TipoCliente.PARTICULAR:
            return f"{self.nombres} {self.apellidos}"
        else:
            return self.razon_social or self.nombre_comercial
    
    @property
    def nombre_completo(self):
        """Retorna el nombre completo según el tipo de cliente"""
        if self.tipo == TipoCliente.PARTICULAR:
            return f"{self.nombres} {self.apellidos}".strip()
        else:
            return self.razon_social or self.nombre_comercial
    
    @property
    def documento_principal(self):
        """Retorna el documento principal según el tipo de cliente"""
        if self.tipo == TipoCliente.PARTICULAR:
            return self.dni
        else:
            return self.ruc
    
    def clean(self):
        from django.core.exceptions import ValidationError
        
        # Validaciones según el tipo de cliente
        if self.tipo == TipoCliente.PARTICULAR:
            if not self.nombres or not self.apellidos:
                raise ValidationError("Los clientes particulares deben tener nombres y apellidos.")
        else:
            if not self.razon_social and not self.nombre_comercial:
                raise ValidationError("Los clientes corporativos deben tener razón social o nombre comercial.")


class ContactoCliente(BaseModel):
    """Contactos adicionales para clientes corporativos"""
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name='contactos',
        verbose_name="Cliente"
    )
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    cargo = models.CharField(max_length=100, blank=True, verbose_name="Cargo")
    telefono = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    email = models.EmailField(blank=True, verbose_name="Email")
    es_principal = models.BooleanField(default=False, verbose_name="Es contacto principal")
    
    class Meta:
        verbose_name = "Contacto de Cliente"
        verbose_name_plural = "Contactos de Clientes"
        db_table = "clientes_contacto_cliente"
        ordering = ['-es_principal', 'apellidos', 'nombres']
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cliente}"


class HistorialCliente(BaseModel):
    """Historial de interacciones con el cliente"""
    
    TIPO_INTERACCION_CHOICES = [
        ('LLAMADA', 'Llamada Telefónica'),
        ('EMAIL', 'Correo Electrónico'),
        ('VISITA', 'Visita al Local'),
        ('REUNION', 'Reunión'),
        ('OTRO', 'Otro'),
    ]
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        related_name='historial',
        verbose_name="Cliente"
    )
    tipo_interaccion = models.CharField(
        max_length=20, 
        choices=TIPO_INTERACCION_CHOICES,
        verbose_name="Tipo de Interacción"
    )
    fecha = models.DateTimeField(verbose_name="Fecha y Hora")
    descripcion = models.TextField(verbose_name="Descripción")
    usuario = models.CharField(max_length=100, verbose_name="Usuario que registra")
    
    class Meta:
        verbose_name = "Historial de Cliente"
        verbose_name_plural = "Historial de Clientes"
        db_table = "clientes_historial_cliente"
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.cliente} - {self.tipo_interaccion} - {self.fecha.strftime('%d/%m/%Y')}"