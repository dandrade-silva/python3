# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
    if usuario.lower() == senha.lower():
        print('A senha não pode ser igual ao nome do usuário. Tente novamente!')
    else:
        break

print('Usuário OK')
print('FIM DO PROGRAMA')
