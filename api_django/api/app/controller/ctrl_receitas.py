import json, requests, ast, re

from app.models import Receita, ModoPreparo, IngredienteReceita, InformacaoReceita

def retorna_indices_ingredientes_concatenados(texto):

    # x = re.split("[a-zA-Záãéóíú\)][0-9]", texto)

    texto_corrigido = texto

    lista_substrings_ocorrencia = re.findall("[a-zA-Záãéóíú\)][0-9]", texto)

    if(lista_substrings_ocorrencia):

        for substring in lista_substrings_ocorrencia:
            indice_substring = texto_corrigido.find(str(substring)) + 1
            texto_corrigido = texto_corrigido[:indice_substring] + '@&' + texto_corrigido[indice_substring:]
        
        lista_ingredientes = texto_corrigido.split("@&")

    else:
        
        lista_ingredientes = [texto]
    
    return lista_ingredientes

def adicionar_espaco_entre_numero_e_string(texto):

    texto_corrigido = texto

    lista_substrings_ocorrencia = re.findall("[0-9][a-zA-Záãéóíú\)]", texto_corrigido)

    for substring in lista_substrings_ocorrencia:
        indice_substring = texto_corrigido.find(str(substring)) + 1
        texto_corrigido = texto_corrigido[:indice_substring] + ' ' + texto_corrigido[indice_substring:]

    return texto_corrigido

def remove_sujeira_str(texto):
    return texto.strip().replace("\xa0", " ")

def get_receitas_base_dados():

    # Making a get request 
    response = requests.get('https://raw.githubusercontent.com/adrianosferreira/afrodite.json/master/afrodite.json')

    receitas = []
    i = 0; maximo_receitas = 100

    indices_json = {'ingredientes': 0, 'modo_preparo': 1, 'outras_informacoes': 2}

    for item in response.json():

        if(i >= maximo_receitas):
            break

        receitas.append(item['nome'])

        receita = Receita.objects.create(nome=remove_sujeira_str(item['nome']))
        receita.save()
        
        lista_ingredientes = []

        for ingrediente in item['secao'][indices_json['ingredientes']]['conteudo']:
            lista_ingredientes_separados = retorna_indices_ingredientes_concatenados(remove_sujeira_str(ingrediente))
            for ingrediente_2 in lista_ingredientes_separados:
                if(ingrediente_2 != ""):
                    lista_ingredientes.append(IngredienteReceita(receita=receita, ingrediente=adicionar_espaco_entre_numero_e_string(ingrediente_2)))
        
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
        if(receita.nome not in dicionario_receitas):
            dicionario_receitas.update({receita.nome:receita.id})

    response = json.dumps(dicionario_receitas)
    
    return response

def receita(id_receita):

    dicionario_receita = {}

    receita = Receita.objects.filter(id=id_receita)

    if(receita.exists()):

        receita = receita[0]

        dicionario_receita.update({'nome': receita.nome})

        ingredientes = IngredienteReceita.objects.filter(receita=receita)

        lista_ingredientes = []
        for ingrediente in ingredientes:
            lista_ingredientes.append(ingrediente.ingrediente)
        
        if(lista_ingredientes):
            dicionario_receita.update({'ingredientes': lista_ingredientes})
        
        modo_preparo = ModoPreparo.objects.filter(receita=receita)

        lista_modo_preparo = []
        for mp in modo_preparo:
            lista_modo_preparo.append(mp.passos)
        
        if(lista_modo_preparo):
            dicionario_receita.update({'modo_preparo': lista_modo_preparo})

        informacoes = InformacaoReceita.objects.filter(receita=receita)

        lista_informacoes = []
        for informacao in informacoes:
            lista_informacoes.append(informacao.informacao)
        
        if(lista_informacoes):
            dicionario_receita.update({'informacoes': lista_informacoes})
    
    response = json.dumps(dicionario_receita)
    
    return response

def buscar_receita(request):

    dicionario_receitas = {}

    palavra = ast.literal_eval(request.body.decode("utf-8"))['palavra']
    # palavra = request.POST['palavra'] # ou request.POST.getlist('palavra', None)

    receitas_com_palavra = Receita.objects.filter(nome__icontains=palavra)
    
    for receita in receitas_com_palavra:
        if(receita.nome not in dicionario_receitas):
            dicionario_receitas.update({receita.nome:receita.id})
    
    ingredientes_com_palavra = IngredienteReceita.objects.filter(ingrediente__icontains=palavra)

    for ingrediente in ingredientes_com_palavra:
        if(ingrediente.receita.nome not in dicionario_receitas):
            dicionario_receitas.update({ingrediente.receita.nome:ingrediente.receita.id})

    response = json.dumps(dicionario_receitas)
    
    return response