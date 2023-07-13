"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    Imprima na tela as informações dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00"""


def menu(txt):
    tamanho = len(txt)+4
    print('=' * tamanho)
    print(f'{txt:^{tamanho}}')
    print('=' * tamanho)


template_holerite = """
(=) Valor Bruto     : R$ {:>8.2f}
(-) IR({:<2.0f}%)         : R$ {:>8.2f}
(-) INSS(10 %)      : R$ {:>8.2f}
(-) Sindicado(3 %)  : R$ {:>8.2f}
(=) Total Descontos : R$ {:>8.2f}
    FGTS(11 %)      : R$ {:>8.2f}
(=) Valor Líquido   : R$ {:>8.2f}"""

menu('FOLHA DE PAGAMENTO')

valor_hora = float(input('Valor hora: R$ '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas
desconto_inss = salario_bruto * 0.1
desconto_sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

#   Calculo do IR
if salario_bruto <= 900.00:
    ir = 0
elif salario_bruto <= 1500.00:
    ir = 0.05
elif salario_bruto <= 2500.00:
    ir = 0.1
else:
    ir = 0.2

desconto_ir = salario_bruto * ir
total_descontos = desconto_inss + desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(template_holerite.format(salario_bruto, ir*100, desconto_ir, desconto_inss, desconto_sindicato, fgts,
                               total_descontos, salario_liquido))
