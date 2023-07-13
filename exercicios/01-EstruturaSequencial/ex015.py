"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
"""

valor_hora = float(input('Informe quanto você ganha por hora trabalhada: R$ '))
horas_trabalhadas = int(input('E quantas horas você trabalha por mês: '))
sal_bruto = valor_hora * horas_trabalhadas
ir = sal_bruto * -0.11
inss = sal_bruto * -0.08
sindicato = sal_bruto * -0.05
sal_liquido = sal_bruto + ir + inss + sindicato

print(f'''
+ Salário Bruto   : R$ {sal_bruto:>8.2f}
- IR (11%)        : R$ {ir:>8.2f}
- INSS (8%)       : R$ {inss:>8.2f}
- Sindicato (5%)  : R$ {sindicato:>8.2f}
= Salário Liquido : R$ {sal_liquido:>8.2f}
''')
