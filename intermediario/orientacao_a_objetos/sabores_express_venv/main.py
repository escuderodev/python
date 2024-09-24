from fastapi import FastAPI, Query
import requests

server = FastAPI()

# modo de requisição: http://127.0.0.1:8000/
@server.get('/')
def hello_world():
    '''
    Endponint de entrada da API.
    '''
    return {'message': 'Bem vindo a minha API com FastApi e Python'}
    
# mode de requisição: http://127.0.0.1:8000/api/restaurantes/
# mode de requisição: http://127.0.0.1:8000/api/restaurantes/?restaurante=KFC
@server.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint que exibe todos os restaurantes, mas também permite buscar por nome do restaurante.
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url) 

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {
            'Restaurante': restaurante,
            'Cardápio': dados_restaurante
        }
    else:
        return {
            'Erro': f'{response.status_code} - {response.text}'
        }        