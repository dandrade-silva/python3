# Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = str(input('Nome: ')).strip()
    if len(nome) < 3:
        print('O nome precisa ter pelo menos 3 caracteres. Tente novamente!')
    else:
        break

while True:
    idade = int(input('Idade: '))
    if idade < 0 or idade > 150:
        print('A idade precisa ser entre 0 a 150. Tente novamente!')
    else:
        break

while True:
    salario = float(input('Salário: R$ '))
    if salario <= 0:
        print('O salário precisa ser maior que R$ 0,00. Tente novamente!')
    else:
        break

while True:
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    if sexo not in 'FM':
        print('Sexo deve ser F ou M. Tente novamente!')
    else:
        break

while True:
    est_civil = str(input('Estado Civil [S/C/V/D]: ')).strip().upper()
    if est_civil not in 'SCVD':
        print('O estado civil deve ser S, C, V ou D. Tente novamente!')
    else:
        break

print('As informações digitadas foram:')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Salário: R$ {salario}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {est_civil}')
