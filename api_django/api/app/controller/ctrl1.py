import json, requests

from app.models import Receita, ModoPreparo, IngredienteReceita, InformacaoReceita

def remove_sujeira_str(texto):
    return texto.strip().replace("\xa0", "")

def get_receitas_base_dados():

    # curl -X POST -H \"Content-Type: application/json\" -d \
    # '{\"destino\":\"1\",\"passagem\":\"2\",\"hospedagem\":\"1\",\"passeios\":\"1,2\" }' \
    # http://localhost:8080/build/webresources/vendas

    # Making a get request 
    response = requests.get('https://raw.githubusercontent.com/adrianosferreira/afrodite.json/master/afrodite.json')

    receitas = []
    i = 0; maximo_receitas = 50

    indices_json = {'ingredientes': 0, 'modo_preparo': 1, 'outras_informacoes': 2}

    for item in response.json():

        if(i >= maximo_receitas):
            break

        receitas.append(item['nome'])

        receita = Receita.objects.create(nome=remove_sujeira_str(item['nome']))
        receita.save()
        
        lista_ingredientes = []

        for ingrediente in item['secao'][indices_json['ingredientes']]['conteudo']:
            item_inserir = remove_sujeira_str(ingrediente)
            if(item_inserir != ""):
                lista_ingredientes.append(IngredienteReceita(receita=receita, ingrediente=item_inserir))
        
        IngredienteReceita.objects.bulk_create(lista_ingredientes)

        lista_modo_preparo = []

        for modo_preparo in item['secao'][indices_json['modo_preparo']]['conteudo']:
            item_inserir = remove_sujeira_str(modo_preparo)
            if(item_inserir != ""):
                lista_modo_preparo.append(ModoPreparo(receita=receita, passos=item_inserir))
        
        ModoPreparo.objects.bulk_create(lista_modo_preparo)

        lista_outras_informarcoes = []

        if(len(item['secao']) > 2):

            for outras_informacoes in item['secao'][indices_json['outras_informacoes']]['conteudo']:
                item_inserir = remove_sujeira_str(outras_informacoes)
                if(item_inserir != ""):
                    lista_outras_informarcoes.append(InformacaoReceita(receita=receita, informacao=item_inserir))
            
            InformacaoReceita.objects.bulk_create(lista_outras_informarcoes)

        i += 1

    response = json.dumps(receitas)
    
    return response

def receitas():

    dicionario_receitas = {}

    receitas_disponiveis = Receita.objects.all()
    
    for receita in receitas_disponiveis:
        dicionario_receitas.update({receita.nome:receita.id})

    response = json.dumps(dicionario_receitas)
    
    return response

def receita(id_receita):

    dicionario_receita = {}

    receita = Receita.objects.filter(id=id_receita)

    if(receita.exists()):

        ingredientes = IngredienteReceita.objects.filter(receita=receita[0])

        lista_ingredientes = []
        for ingrediente in ingredientes:
            lista_ingredientes.append(ingrediente.ingrediente)
        
        if(lista_ingredientes):
            dicionario_receita.update({'ingredientes': lista_ingredientes})
        
        modo_preparo = ModoPreparo.objects.filter(receita=receita[0])

        lista_modo_preparo = []
        for mp in modo_preparo:
            lista_modo_preparo.append(mp.passos)
        
        if(lista_modo_preparo):
            dicionario_receita.update({'modo_preparo': lista_modo_preparo})

        informacoes = InformacaoReceita.objects.filter(receita=receita[0])

        lista_informacoes = []
        for informacao in informacoes:
            lista_informacoes.append(informacao.informacao)
        
        if(lista_informacoes):
            dicionario_receita.update({'informacoes': lista_informacoes})
    
    response = json.dumps(dicionario_receita)
    
    return response

