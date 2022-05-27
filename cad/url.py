from django.urls import path
from cad.views.cliente.views import *
from cad.views.contrato.views import *
from cad.views.solicitudes.views import *
from cad.views.ingreso.views import *
from cad.views.extracciones.views import *
from cad.views.retorno.views import *
from cad.views.dashboard.views import *

app_name = 'cad'

urlpatterns = [
    # Cliente
    path('cliente/list/', ClienteListView.as_view(), name='cliente_list'),
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/edit/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # Contrato
    path('contrato/list/', ContratoListView.as_view(), name='contrato_list'),
    path('contrato/add/', ContratoCreateView.as_view(), name='contrato_create'),
    path('contrato/edit/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('contrato/delete/<int:pk>/', ContratoDeleteView.as_view(), name='contrato_delete'),

    # Solicitudes
    path('solicitudes/list/', SolicitudesListView.as_view(), name='solicitudes_list'),
    path('solicitudes/add/', SolicitudesCreateView.as_view(), name='solicitudes_create'),
    path('solicitudes/edit/<int:pk>/', SolicitudesUpdateView.as_view(), name='solicitudes_update'),
    path('solicitudes/delete/<int:pk>/', SolicitudesDeleteView.as_view(), name='solicitudes_delete'),

    # Ingreso
    path('ingreso/list/', IngresoListView.as_view(), name='ingreso_list'),
    path('ingreso/add/', IngresoCreateView.as_view(), name='ingreso_create'),
    path('ingreso/edit/<int:pk>/', IngresoUpdateView.as_view(), name='ingreso_update'),
    path('ingreso/delete/<int:pk>/', IngresoDeleteView.as_view(), name='ingreso_delete'),

    # Extracciones
    path('extracciones/list/', ExtraListView.as_view(), name='extra_list'),
    path('extracciones/add/', ExtraCreateView.as_view(), name='extra_create'),
    path('extraccciones/edit/<int:pk>/', ExtraUpdateView.as_view(), name='extra_update'),
    path('extraciones/delete/<int:pk>/', ExtraDeleteView.as_view(), name='extra_delete'),

    # Retorno
    path('retorno/list/', RetornoListView.as_view(), name='retorno_list'),
    path('retorno/add/', RetornoCreateView.as_view(), name='retorno_create'),
    path('retorno/edit/<int:pk>/', RetornoUpdateView.as_view(), name='retorno_update'),
    path('retorno/delete/<int:pk>/', RetornoDeleteView.as_view(), name='retorno_delete'),

    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
