from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.dashboard_reportes, name='dashboard'),
    path('financieros/', views.reportes_financieros, name='financieros'),
    path('inventario/', views.reportes_inventario, name='inventario'),
    path('produccion/', views.reportes_produccion, name='produccion'),
]
