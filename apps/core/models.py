from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class TenantManager(models.Manager):
    """Manager que filtra automáticamente por tenant_id"""
    
    def get_queryset(self):
        # Por ahora retornamos todos los objetos sin filtrar
        # El filtrado por tenant se implementará más adelante
        return super().get_queryset()


class TenantModel(models.Model):
    """Modelo base que incluye soporte multi-tenant"""
    
    tenant_id = models.CharField(max_length=50, db_index=True, help_text="ID del tenant para multi-tenancy")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TenantManager()
    all_objects = models.Manager()  # Manager sin filtro de tenant
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        # Asignar tenant_id si no está establecido
        if not self.tenant_id and hasattr(self._state, 'current_tenant_id'):
            self.tenant_id = self._state.current_tenant_id
        super().save(*args, **kwargs)


class Tenant(models.Model):
    """Modelo para gestionar los tenants (empresas/organizaciones)"""
    
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre de la empresa")
    description = models.TextField(blank=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Configuraciones específicas del tenant
    settings = models.JSONField(default=dict, blank=True, verbose_name="Configuraciones")
    
    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"
        db_table = "core_tenant"
    
    def __str__(self):
        return self.name


class TenantUser(models.Model):
    """Relación entre usuarios y tenants"""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False, verbose_name="Es administrador del tenant")
    is_active = models.BooleanField(default=True, verbose_name="Activo en este tenant")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Usuario del Tenant"
        verbose_name_plural = "Usuarios del Tenant"
        unique_together = ('user', 'tenant')
        db_table = "core_tenant_user"
    
    def __str__(self):
        return f"{self.user.username} - {self.tenant.name}"


class BaseModel(TenantModel):
    """Modelo base extendido con campos comunes"""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    
    class Meta:
        abstract = True


# Modelos para auditoria y logs
class AuditLog(TenantModel):
    """Modelo para auditoría de cambios"""
    
    ACTION_CHOICES = [
        ('CREATE', 'Crear'),
        ('UPDATE', 'Actualizar'),
        ('DELETE', 'Eliminar'),
        ('VIEW', 'Ver'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Usuario")
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, verbose_name="Acción")
    model_name = models.CharField(max_length=100, verbose_name="Modelo")
    object_id = models.CharField(max_length=100, verbose_name="ID del objeto")
    old_values = models.JSONField(null=True, blank=True, verbose_name="Valores anteriores")
    new_values = models.JSONField(null=True, blank=True, verbose_name="Valores nuevos")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y hora")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Dirección IP")
    
    class Meta:
        verbose_name = "Log de Auditoría"
        verbose_name_plural = "Logs de Auditoría"
        db_table = "core_audit_log"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name} - {self.timestamp}"