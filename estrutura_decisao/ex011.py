"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

print('============================')
print(f'{"REAJUSTE SALARIAL":^28}')
print('============================')

salario_atual = float(input('Salário Bruto atual: R$ '))

if salario_atual <= 280.00:
    reajuste = 0.2
elif salario_atual < 700.00:
    reajuste = 0.15
elif salario_atual < 1500.00:
    reajuste = 0.1
else:
    reajuste = 0.05

print(f'''============================
Salário atual: R${salario_atual:>8.2f}
Reajuste (R$): R${salario_atual * reajuste:>8.2f}
Reajuste  (%):  %{reajuste * 100:>8.2f}
Novo Salário : R${salario_atual * (1 + reajuste):>8.2f}
============================''')
