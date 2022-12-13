import json
#import pandas as pd
import sys
import requests
from flask import Flask


app = Flask(__name__)

#Gerar Token ---------------------------------------------------------------------------------
 
url = 'https://h-autocontrole-mapa.estaleiro.serpro.gov.br/sda-gateway-api/sessions'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

#Substituir credenciais
json_data = {
    'clientId': 'bb0be971-6077-4256-99ab-9726489bafb5',
    'clientSecret': '8d5e5ba6-0c0c-44bc-a3fa-c56ecf8a9529',
}

#Fazer requisição do token
response = requests.post(
    url,
    headers=headers,
    json=json_data,
)

token = response.json()['token']


@app.route('/get_adesao', methods=['GET'])
def get_adesao():
    

    #Evento Adesão ---------------------------------------------------------------------------------

    url = 'https://h-autocontrole-mapa.estaleiro.serpro.gov.br/sda-gateway-api/eventos/v1/registros/protocolos-privados/3/credenciamento/adesao'

    body= {
    "dados": 
        {
        "supervisora": "ABIEC",
        "finalidade": "CARNE BOVINA PARA A ARABIA SAUDITA",
        "sif": "0049",
        "dataAdesao": "2022-11-23T13:45:01-03:00",
        "statusAdesao": "ADESÃO INICIAL"
        }
    }

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }


    #Fazer post adesao
    response = requests.post(
        url,
        headers=headers,
        json=body,
    )


    adesao = response.json()
    


    return adesao


if __name__=='__main__':
   app.run(debug=True)