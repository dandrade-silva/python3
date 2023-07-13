# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    n = int(input('Digite um número entre 0 e 10: '))
    if n not in range(0, 11):
        print('Valor inválido!')
    else:
        print(f'Você digitou o valor {n}')
        break

print('FIM DO PROGRAMA')
