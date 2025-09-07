from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.listar_clientes, name='listar'),
    path('nuevo/', views.crear_cliente, name='crear'),
    path('<uuid:pk>/', views.detalle_cliente, name='detalle'),
    path('<uuid:pk>/editar/', views.editar_cliente, name='editar'),
    path('<uuid:pk>/eliminar/', views.eliminar_cliente, name='eliminar'),
]
