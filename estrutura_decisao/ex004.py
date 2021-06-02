#   Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('--------------------')
print(' VOGAL OU CONSOANTE ')
print('--------------------')

letra = str(input('Digite uma letra: ')).upper()

vogais = ('A', 'E', 'I', 'O', 'U')

if letra in vogais:
    print(f'A letra {letra} é uma vogal.')
else:
    print(f'A letra {letra} é uma consoante.')
