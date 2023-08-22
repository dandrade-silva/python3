"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""


# Variáveis
pop_a = 80000
pop_a_percentual_cresc_anual = 0.03
pop_b = 200000
pop_b_percentual_cresc_anual = 0.015

anos = 0

while pop_a < pop_b:
    pop_a *= (1+pop_a_percentual_cresc_anual)
    pop_b *= (1+pop_b_percentual_cresc_anual)
    anos += 1


print(f'A população do país A precisou de {anos} anos para superar a população do país B')
