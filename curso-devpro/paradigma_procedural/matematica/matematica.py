def soma(*args):
    total = 0
    for valor in args:
        total += valor
    return total


# Só sera executado quando for chamado direto pelo pacote.
if __name__ == '__main__':
    print(soma(1, 2, 3))
