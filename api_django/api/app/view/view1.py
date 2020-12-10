from django.shortcuts import render
from django.http import HttpResponse, response
# from requests.api import request

from app.controller import ctrl1

# Create your views here.

def get_receitas_base_dados(request):
    
    response = ctrl1.get_receitas_base_dados()

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def receitas(request):
    
    response = ctrl1.receitas()

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def receita(request, id_receita):
    
    response = ctrl1.receita(id_receita)

    return HttpResponse(response, content_type='application/json; charset=utf-8')

def buscar_receita(request):

    response = ctrl1.buscar_receita(request)

    return HttpResponse(response, content_type='application/json; charset=utf-8')