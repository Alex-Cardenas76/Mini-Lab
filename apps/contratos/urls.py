from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    path('', views.listar_contratos, name='listar'),
    path('nuevo/', views.crear_contrato, name='crear'),
    path('<uuid:pk>/', views.detalle_contrato, name='detalle'),
    path('<uuid:pk>/editar/', views.editar_contrato, name='editar'),
]
