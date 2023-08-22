# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

print('==================')
print(' DIGITE 5 NÚMEROS ')
print('==================')

for v in range(5):
    n = input(f'Informe o {v+1}º número: ')
    numeros.append(n)

print(f'Os números digitados foram: {numeros}')
