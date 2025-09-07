from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
import threading

# Variable local del hilo para almacenar el tenant_id actual
_thread_local = threading.local()


class TenantMiddleware(MiddlewareMixin):
    """
    Middleware para manejar multi-tenancy a nivel de fila (row-level).
    Extrae el tenant_id de la sesión, cookie o header y lo hace disponible
    para todos los modelos que hereden de TenantModel.
    """
    
    def process_request(self, request):
        tenant_id = self.get_tenant_id(request)
        
        # Establecer el tenant_id en el thread local
        _thread_local.tenant_id = tenant_id
        
        # También lo agregamos al request para fácil acceso
        request.tenant_id = tenant_id
        
        # Si no hay tenant_id y no estamos en login, redirigir al login
        if not tenant_id and not request.path.startswith('/login/') and not request.path.startswith('/admin/'):
            return redirect(reverse('login'))
        
        return None
    
    def get_tenant_id(self, request):
        """
        Obtiene el tenant_id desde múltiples fuentes en orden de prioridad:
        1. Sesión del usuario
        2. Cookie
        3. Header HTTP
        """
        # 1. Desde la sesión (más seguro)
        tenant_id = request.session.get('tenant_id')
        if tenant_id:
            return tenant_id
        
        # 2. Desde cookie
        tenant_id = request.COOKIES.get(settings.TENANT_COOKIE_NAME)
        if tenant_id:
            # Almacenar en sesión para próximas requests
            request.session['tenant_id'] = tenant_id
            return tenant_id
        
        # 3. Desde header HTTP (para APIs)
        tenant_id = request.META.get(settings.TENANT_HEADER_NAME)
        if tenant_id:
            return tenant_id
        
        return None
    
    def process_response(self, request, response):
        # Limpiar el thread local al final del request
        if hasattr(_thread_local, 'tenant_id'):
            delattr(_thread_local, 'tenant_id')
        return response


def get_current_tenant_id():
    """
    Función helper para obtener el tenant_id actual desde cualquier parte del código
    """
    return getattr(_thread_local, 'tenant_id', None)


# Monkey patch para inyectar el tenant_id en todos los modelos que hereden de TenantModel
original_init = models.Model.__init__

def patched_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    
    # Solo aplicar a modelos que tienen el campo tenant_id
    if hasattr(self, 'tenant_id') and hasattr(self._meta, 'get_field'):
        try:
            self._meta.get_field('tenant_id')
            # Establecer el tenant_id automáticamente si no está definido
            if not getattr(self, 'tenant_id', None):
                current_tenant_id = get_current_tenant_id()
                if current_tenant_id:
                    self.tenant_id = current_tenant_id
        except:
            pass

models.Model.__init__ = patched_init
