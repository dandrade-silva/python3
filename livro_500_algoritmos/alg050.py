"""
Entrar com base e a altura de um retângulo e imprimir a seguinte saída:
perimetro:
area:
diagonal:

Calculos:
perimetro = 2 x (base x altura)
area = base * altura
diagonal = raiz (base**2 + altura**2)
"""
from math import sqrt


def header(exercicio):
    tamanho = len(exercicio) + 10
    print("=" * tamanho)
    print(f'{exercicio.center(tamanho)}')
    print("=" * tamanho)


header("ALGORITMO 050")

# Entrada de Dados
base = int(input('Digite base: '))
altura = int(input('Digite altura: '))

# Calculos
perimetro = 2 * (base + altura)
area = base * altura
diagonal = sqrt(base**2 + altura**2)

# Resultado na tela
print("\n==========RESULTADO==========")
print(f'perimetro: {perimetro}')
print(f'area: {area}')
print(f'diagonal: {diagonal:.2f}')
print("=============================")
