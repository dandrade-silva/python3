# API de Cotações de Moedas

import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")
cotacoes = cotacoes.json()
dolar = cotacoes["USDBRL"]

print(dolar['bid'])
