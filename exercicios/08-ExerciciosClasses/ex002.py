# Classe Quadrado: Crie uma classe que modele um quadrado:
#
#     a Atributos: Tamanho do lado
#     b Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def muda_valor_lado(self, lado):
        self.lado = lado

    def valor_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado ** 2


if __name__ == '__main__':
    quadrado = Quadrado(8)
    print(quadrado.valor_lado())
    print(quadrado.calcula_area())
    quadrado.muda_valor_lado(10)
    print(quadrado.calcula_area())

