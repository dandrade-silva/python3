#   Faça um programa para a leitura de duas notas parciais de um aluno.
#   O programa deve calcular a média alcançada por aluno e apresentar:
#    2 A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    3 A mensagem "Reprovado", se a média for menor do que sete;
#    1 A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Informe sua 1ª nota: '))
n2 = float(input('Informe sua 2ª nota: '))
media = (n1 + n2) / 2

if media >= 10:
    sit = 'Aprovado com distinção'
elif media >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'

print(f'Você teve a média {media}. Está {sit}!')
