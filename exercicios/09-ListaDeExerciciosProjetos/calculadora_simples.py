def somar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    return x / y


# Dicionário com as operações
operacoes = {
    1: "Soma",
    2: "Subtração",
    3: "Multiplicação",
    4: "Divisão"
}

# MENU
print(f'\n{" CALCULADORA EM PYTHON ":=^50}')
print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")


# Input do usuário
while True:
    try:
        opcao = int(input("\nDigite a operação desejada(1/2/3/4): "))
        if 0 < opcao <= 4:
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite outro número: '))
            break
        else:
            print('[ERRO] Opção inválida. Tente novamente!')
    except:
        print('[ERRO] Digite apenas o número da opção desejada!')


# Calculo da operação selecionada
match opcao:
    case 1:
        resultado = somar(n1, n2)
    case 2:
        resultado = subtrair(n1, n2)
    case 3:
        resultado = multiplicar(n1, n2)
    case 4:
        resultado = dividir(n1, n2)

# Imprime o resultado na tela
print(f'A {operacoes[opcao]} entre {n1} e {n2} é igual a {resultado}')
