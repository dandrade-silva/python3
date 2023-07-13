#   Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('=' * 20)
print(f'{"Média Bimestral":^20}')
print('=' * 20)

n1 = float(input('Nota Prova1: '))
n2 = float(input('Nota Prova2: '))
n3 = float(input('Nota Prova3: '))
n4 = float(input('Nota Prova4: '))
media = (n1 + n2 + n3 + n4) / 4

print(f'Sua média foi {media}')
