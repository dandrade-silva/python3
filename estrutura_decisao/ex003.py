#   Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#   Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

str = str(input('Informe seu sexo [M/F]: ')).upper()
sexo = {'M': 'Masculino', 'F': 'Feminino'}

if str not in 'MF':
    print('Sexo inválido')
else:
    print(f'Você é do sexo {sexo[str]}.')
