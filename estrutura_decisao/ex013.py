# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


def menu(txt):
    tamanho = len(txt)+4
    print('=' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('=' * tamanho)


dias_da_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
menu('DIA DA SEMANA')

for dia in enumerate(dias_da_semana):
    print(f'[{dia[0]+1}] {dia[1]}')

hoje = int(input('Que dia é hoje? '))

if hoje in range(1, 8):
    print(f'Hoje é {dias_da_semana[hoje-1]}!')
else:
    print('Dia inválido!')
