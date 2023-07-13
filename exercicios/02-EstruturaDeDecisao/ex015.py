# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#     Dicas:
#     Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#     Triângulo Equilátero: três lados iguais;
#     Triângulo Isósceles: quaisquer dois lados iguais;
#     Triângulo Escaleno: três lados diferentes;


def menu(txt):
    tamanho = len(txt)+4
    print('=' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('=' * tamanho)


menu('TIPO DE TRIÂNGULO')

l1 = float(input('Tamanho do 1º lado:'))
l2 = float(input('Tamanho do 2º lado:'))
l3 = float(input('Tamanho do 3º lado:'))

# | l2 - l3 | < l1 < l2 + l3
# | l1 - l3 | < l2 < l1 + l3
# | l1 - l2 | < l3 < l1 + l2

if l1 == 0 or l2 == 0 or l3 == 0:
    print('Digite um valor maior que zero!')
elif (l2 - l3) < l1 < (l2 + l3) or (l1 - l3) < l2 < (l1 + l3) or (l1 - l2) < l3 < (l1 + l2):
    if l1 == l2 == l3:
        print('Triângulo Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triãngulo Isósceles')
    elif l1 != l2 and l2 != l3:
        print('Triãngulo Escaleno')
else:
    print('Não é possível formar um triângulo!')
