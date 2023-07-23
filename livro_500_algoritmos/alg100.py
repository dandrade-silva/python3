"""
Ler um número inteiro de 4 casas e 
imprimir se é ou não múltiplo de 4 
imprimir o número formado pelos algarismos que estão nas casas de milhar e das centenas
"""


def header(exercicio):
    tamanho = len(exercicio) + 10
    print("=" * tamanho)
    print(f'{exercicio.center(tamanho)}')
    print("=" * tamanho)


header("ALGORITMO 100")

# Entrada de dados
numero = int(input('Digite um número de 4 algarismos: '))

# Calculos
multiplo_4 = (numero % 4) == 0

# Imprimindo na tela
if multiplo_4:
    print(f'O número {numero} é multiplo de 4.')
else:
    print(f'O número não é multiplo de 4: {numero}')

print(f'E os números das casas de milhar e centenas é {int(numero/100)}')
