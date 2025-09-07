from django.urls import path
from . import views

app_name = 'produccion'

urlpatterns = [
    path('', views.listar_ordenes, name='listar'),
    path('nueva/', views.crear_orden, name='crear'),
    path('<uuid:pk>/', views.detalle_orden, name='detalle'),
    path('productos-terminados/', views.productos_terminados, name='productos_terminados'),
]
