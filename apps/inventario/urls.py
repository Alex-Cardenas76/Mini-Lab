from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.listar_inventario, name='listar'),
    path('alertas/', views.alertas_stock, name='alertas'),
    path('varillas/', views.listar_varillas, name='varillas'),
    path('pinturas/', views.listar_pinturas, name='pinturas'),
    path('materiales/', views.listar_materiales, name='materiales'),
    path('movimientos/', views.listar_movimientos, name='movimientos'),
]
