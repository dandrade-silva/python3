# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

vlr_hora = float(input('Digite quanto você ganha por hora: '))
horas_trab = int(input('Horas trabalhadas no mês: '))
salario = vlr_hora * horas_trab

print(f'Seu salário mensal é R$ {salario:.2f}')
