#   Faça um programa que pergunte o preço de três produtos e
#   informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produtos = []
for valor in range(0, 3):
    produtos.append(int(input(f'Preço do {valor+1}º produto: R$ ')))

print(f'Você deve comprar o produto com valor de R$ {min(produtos):.2f}')
