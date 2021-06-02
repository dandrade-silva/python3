#   Faça um Programa que leia três números e mostre o maior deles.

numeros = []
for num in range(0, 3):
    numeros.append(int(input('Digite um número: ')))

print(f'O maior número digitado foi o {max(numeros)}')
