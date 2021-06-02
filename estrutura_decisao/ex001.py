#   Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 < n2:
    print(f'O maior número digitado foi o {n2}.')
elif n2 < n1:
    print(f'O maior número digitado foi o {n1}')
else:
    print(f'Os números digitados são iguais.')
