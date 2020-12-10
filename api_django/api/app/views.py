from django.shortcuts import render
from django.http import HttpResponse
import json, requests

# Create your views here.


def index(request):
    
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # convert into JSON:
    data = json.dumps(x)

    # the result is a JSON string:
    print(data) 

    return HttpResponse(data, content_type='application/json')

def dados(request):
    
    print(request)

    # curl -X POST -H \"Content-Type: application/json\" -d \
    # '{\"destino\":\"1\",\"passagem\":\"2\",\"hospedagem\":\"1\",\"passeios\":\"1,2\" }' \
    # http://localhost:8080/build/webresources/vendas

    # Making a get request 
    response = requests.get('https://raw.githubusercontent.com/adrianosferreira/afrodite.json/master/afrodite.json') 
    
    # print response 
    # print(response)
    
    # print json content 
    # print(response.json())

    for i in response.json():
        print(i['_id'])
        print(i['nome'])
        print(i['secao'])
        print(i['secao'][0])
        break

    return HttpResponse(response, content_type='application/json')