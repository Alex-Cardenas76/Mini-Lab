from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.listar_pedidos, name='listar'),
    path('nuevo/', views.crear_pedido, name='crear'),
    path('<uuid:pk>/', views.detalle_pedido, name='detalle'),
    path('<uuid:pk>/editar/', views.editar_pedido, name='editar'),
    path('<uuid:pk>/eliminar/', views.eliminar_pedido, name='eliminar'),
]
