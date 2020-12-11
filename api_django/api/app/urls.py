from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from app.view import view_receitas

urlpatterns = [
    path('', csrf_exempt(view_receitas.receitas), name='receitas'),
    path('get_receitas/', csrf_exempt(view_receitas.get_receitas_base_dados), name='get_receitas_base_dados'),
    path('receita/<int:id_receita>/', csrf_exempt(view_receitas.receita), name='receita'),
    path('buscar_receita/', csrf_exempt(view_receitas.buscar_receita), name='buscar_receita'),
]