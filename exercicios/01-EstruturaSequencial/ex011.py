#   Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   1. O dobro do primeiro com metade do segundo .
#   2. A soma do triplo do primeiro com o terceiro.
#   3. O terceiro elevado ao cubo.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um : '))

print(f'O dobro do primeiro com metade do segundo = {((n1*2) + (n2/2))}')
print(f'A soma do triplo do primeiro com o terceiro = {((n1*3) + n3)}')
print(f'O terceiro elevado ao cubo = {n3**3}')
