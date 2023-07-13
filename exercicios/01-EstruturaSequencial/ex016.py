#   Faça um programa para uma loja de tintas. O programa deverá..
#   Pedir o tamanho em m² da área a ser pintada.
#   Considere que a cobertura da tinta é de 1lt para cada 3m² e que a tinta é vendida em latas de 18lt. Custo = 80,00
#   Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


from math import ceil   # Importando funcão ceil da biblioteca math

#   Menu do programa
print('=' * 45)
print(f'{"CALCULADORA DE TINTAS":^45}')
print('=' * 45)

#   Pedindo informação ao usuário.
area = float(input('Tamanho da àrea(m²) a ser pintada: '))

# Atribuindo valores em variáveis.
qtde_latas = ceil((area / 3) / 18)  # ceil arredonda um número para cima até o próximo número inteiro.
total_pgto = qtde_latas * 80

# Mostrando resultado na tela
print(f'Você vai precisar de {qtde_latas} lata(s) de 18 litros.')
print(f'O valor total para pagamento é R$ {total_pgto:.2f}')
