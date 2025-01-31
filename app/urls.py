from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categoria/', CategoriaView.as_view(), name='categoria'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('cobertura/', CoberturaView.as_view(), name='cobertura'),
    path('colaborador/', ColaboradorView.as_view(), name='colaborador'),
    path('divulgacao/', DivulgacaoView.as_view(), name='divulgacao'),
    path('evento/', EventoView.as_view(), name='evento'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('local/', LocalView.as_view(), name='local'),
    path('material/', MaterialView.as_view(), name='material'),
    path('meioDivulgacao/', MeioDivulgacaoView.as_view(), name='meio_divulgacao'),
    path('organizador/', OrganizadorView.as_view(), name='organizador'),
    path('parceria/', ParceriaView.as_view(), name='parceria'),
    path('publico/', PublicoView.as_view(), name='publico'),
    path('tipoCobertura/', TipoCoberturaView.as_view(), name='tipo_cobertura'),
    path('tipoParceria/', TipoParceriaView.as_view(), name='tipo_parceria'),
    path('uf/', UFView.as_view(), name='uf'),
]