# Classe Bola: Crie uma classe que modele uma bola:
#
#     Atributos: Cor, circunferência, material
#     Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor


if __name__ == '__main__':
    bola = Bola('verde', 68, 'couro')
    print(bola.cor)
    bola.troca_cor('azul')
    print(bola.mostra_cor())
