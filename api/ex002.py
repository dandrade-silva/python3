# Api CEP

import requests
import json


cep = input('Digite um CEP sem traços e sem espaços: ')
api_cep = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
cep = api_cep.json()

print(f'Informações do CEP {cep["cep"]}:')
print(f'{cep["address"]}')
print(f'{cep["city"]}/{cep["state"]}')
print(f'{cep["district"]}')
print('')
print('FIM DO PROGRAMA')
