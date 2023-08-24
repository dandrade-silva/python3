# Parametros Variáveis

def soma(*args):    # Por convenção, os parâmetros variaveis são chamados de args e possuem um *
    total = 0
    for valor in args:
        total += valor
    print(f'A soma dos números é igual a {total}')


def f(**kwargs):
    # Por convenção, os parâmetros variaveis do TIPO "Nomeado" são chamados de kargs e possuem dois **
    # Ele é do tipo dicionário, por isso, só aceita receber parâmetros nomeados, por exemplo: nome = "Danilo"
    print(kwargs)
    print(type(kwargs))


def f2(*args, **kwargs):
    # Também podemos combinar args e kwargs
    print(args)
    print(kwargs)


# f2(args=(1, 2, 3), nome='Danilo', idade=3)

# Para passar uma lista de valores na função f2, temos que realizar o despacotamento.
# Segue um exemplo
args = (2, 4, 10, 20)
kwargs = {'nome': 'Danilo', 'idade': 30}

f2(*args, **kwargs)
