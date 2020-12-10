from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views
from app.view import view1

urlpatterns = [
    path('', csrf_exempt(view1.receitas), name='receitas'),
    path('get_receitas/', csrf_exempt(view1.get_receitas_base_dados), name='get_receitas_base_dados'),
    path('receita/<int:id_receita>/', csrf_exempt(view1.receita), name='receita'),
    path('buscar_receita/', csrf_exempt(view1.buscar_receita), name='buscar_receita'),
]