from django.shortcuts import render
from django.http import HttpResponse, response
# from requests.api import request

from app.controller import ctrl_receitas

# Create your views here.

def get_receitas_base_dados(request):
    
    response = ctrl_receitas.get_receitas_base_dados()

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def receitas(request):
    
    response = ctrl_receitas.receitas()

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def receita(request, id_receita):
    
    response = ctrl_receitas.receita(id_receita)

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def buscar_receita(request):

    response = ctrl_receitas.buscar_receita(request)

    return HttpResponse(response, content_type='application/json; charset=utf-8')