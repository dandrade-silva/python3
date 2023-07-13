# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)


c = float(input('Informe uma tempertura em Celsius: '))
f = (c * 9 / 5) + 32

print(f'{c:.2f}ºC = {f:.2f}ºF')
