# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

r = float(input('Digite o raio do círculo: '))
area = math.pi * pow(r, 2)

print(f'A área do círculo é {area:.2f}')
