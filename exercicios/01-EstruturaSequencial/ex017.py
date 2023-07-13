"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
1. Comprar apenas latas de 18 litros;
2. Comprar apenas galões de 3,6 litros;
3. Misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias """


from math import ceil   # Importando funcão ceil da biblioteca math

#   Menu do programa
print('=' * 50)
print(f'{"CALCULADORA DE TINTAS":^50}')
print('=' * 50)

#   Pedindo informação ao usuário.
area = float(input('Tamanho da àrea(m²) a ser pintada: '))

# Atribuindo valores em variáveis.

# 1. Comprar apenas latas de 18 litros.
qtde_latas18 = ceil((area / 6 * 1.1) / 18)  # ceil arredonda um número para cima até o próximo número inteiro.
total_pgto = qtde_latas18 * 80

# Mostrando resultado na tela
print(f'Comprando apenas latas de 18 litros.')
print(f'Você vai precisar de {qtde_latas18} lata(s).')
print(f'O valor total para pagamento é R$ {total_pgto:.2f}')
print(f'==================================================')

# 2. Comprar apenas latas de 3,6 litros.
qtde_latas3 = ceil((area / 6 * 1.1) / 3.6)  # ceil arredonda um número para cima até o próximo número inteiro.
total_pgto = qtde_latas3 * 25

print(f'Comprando apenas latas de 3.6l.')
print(f'Você vai precisar de {qtde_latas3} lata(s).')
print(f'O valor total para pagamento é R$ {total_pgto:.2f}')
print(f'==================================================')

# 3. Comprar  latas de 18l e 3,6l.
qtde_latas18 = int((area / 6 * 1.1) / 18)
sobra = (area / 6 * 1.1) - (qtde_latas18 * 18)
qtde_latas3 = ceil(sobra / 3.6)
total_pgto = (qtde_latas18 * 80) + (qtde_latas3 * 25)

print(f'Comprando latas de 18l e 3,6l.')
print(f'Você vai precisar de {qtde_latas18} lata(s) de 18 litros '
      f'\nE {qtde_latas3} lata(s) de 3,6 litros.')
print(f'O valor total para pagamento é R$ {total_pgto:.2f}')
print(f'==================================================')
