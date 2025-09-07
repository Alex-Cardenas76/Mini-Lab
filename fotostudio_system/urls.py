"""
URL configuration for fotostudio_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import dashboard_view, login_view, logout_view, configuracion_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs principales
    path('', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('configuracion/', configuracion_view, name='configuracion'),
    
    # URLs de las apps
    path('clientes/', include('apps.clientes.urls', namespace='clientes')),
    path('pedidos/', include('apps.pedidos.urls', namespace='pedidos')),
    path('contratos/', include('apps.contratos.urls', namespace='contratos')),
    path('inventario/', include('apps.inventario.urls', namespace='inventario')),
    path('produccion/', include('apps.produccion.urls', namespace='produccion')),
    path('agenda/', include('apps.agenda.urls', namespace='agenda')),
    path('reportes/', include('apps.reportes.urls', namespace='reportes')),
]

# Servir archivos media y static en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])