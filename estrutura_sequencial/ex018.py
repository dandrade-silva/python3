"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

from math import ceil

print('=' * 50)
print(f'{"TEMPO DE DOWNLOAD":^50}')
print('=' * 50)

tamanho_arquivo = int(input('Tamanho do arquivo em MB: '))
velocidade_internet = int(input('Velocidade da conexão em Mbps: '))
tempo_download = tamanho_arquivo / (velocidade_internet / 8)

min = int(tempo_download / 60)
seg = ceil(tempo_download - (min * 60))

print(f'Tempo para download é de {min} minuto(s) e {seg} segundo(s)')
