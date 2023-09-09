# Imprimir todas as tabuadas de multiplicar de 1 até 10


def header(exercicio):
    tamanho = len(exercicio) + 10
    print("=" * tamanho)
    print(f'{exercicio.center(tamanho)}')
    print("=" * tamanho)


header("ALGORITMO 250")

for tabuada in range(1, 11):
    for multiplicador in range(1, 11):
        print(f'{tabuada} x {multiplicador} = {tabuada * multiplicador}')
    print('=' * 15)
