#   Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []
for n in range(0, 3):
    numeros.append(int(input(f'Digite o {n+1}º número: ')))

numeros = sorted(numeros, reverse=True)

print('Números em ordem decrescente: ', end='')
for valor in numeros:
    print(valor, end='...')
