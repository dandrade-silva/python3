"""
Tamanho de strings. 
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""


def cabecalho(msg):
    largura = len(msg) + 10
    print("=" * largura)
    print(f"{msg:^{largura}}")
    print("=" * largura)


cabecalho("Comparando Strings")

str1 = str(input("Texto 1: "))
str2 = str(input("Texto 2: "))

print(f'Texto 1: {str1}')
print(f'Texto 2: {str2}')
print(f'Tamanho de "{str1}": {len(str1)} caracteres')
print(f'Tamanho de "{str2}": {len(str2)} caracteres')

tamanho = "As duas strings são de tamanhos diferentes." if len(
    str1) != len(str2) else "As duas strings são do mesmo tamanho."
conteudo = "As duas strings possuem conteúdo diferente." if str1 != str2 else "As duas strings possuem o mesmo conteúdo."

print(tamanho)
print(conteudo)
