from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.listar_eventos, name='listar'),
    path('nuevo/', views.crear_evento, name='crear'),
    path('<uuid:pk>/', views.detalle_evento, name='detalle'),
]
