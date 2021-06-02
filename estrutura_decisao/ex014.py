"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C. E “REPROVADO” se o conceito for D ou E. """


def menu(txt):
    tamanho = len(txt)+4
    print('=' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('=' * tamanho)


menu('MÉDIA DO SEMESTRE')

n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))

media = (n1 + n2) / 2

# Calculando o conceito
if media <= 4:
    conceito = 'E'
elif media <= 6:
    conceito = 'D'
elif media <= 7.5:
    conceito = 'C'
elif media <= 9:
    conceito = 'B'
else:
    conceito = 'A'

# Calculando a situação
if conceito in 'ABC':
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(f'Com as notas {n1} e {n2}, sua média ficou em {media}.')
print(f'Seu conceito foi {conceito}, e você está {situacao}!')
