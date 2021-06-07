# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def mudar_lados(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def mostrar_lados(self):
        return f'{self.lado1} e {self.lado2}'

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_perimetro(self):
        return self.lado1 + self.lado1 + self.lado2 + self.lado2


if __name__ == '__main__':
    retangulo = Retangulo(5, 12)
    print(retangulo.mostrar_lados())
    print(retangulo.calcular_area())
    print(retangulo.calcular_perimetro())
    retangulo.mudar_lados(10, 20)
    print(retangulo.mostrar_lados())
    print(retangulo.calcular_area())
    print(retangulo.calcular_perimetro())
