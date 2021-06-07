# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, emagrecer, crescer.
# Obs:Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.05
        self.idade += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        self.altura += 0.05


if __name__ == '__main__':
    danilo = Pessoa(nome='Danilo', idade=28, peso=80, altura=1.66)
    print(danilo.idade)
    danilo.envelhecer()
    print(danilo.idade)
    print(danilo.peso)
    danilo.emagrecer()
    print(danilo.peso)
    danilo.crescer()
    print(danilo.altura)
    danilo.crescer()
    print(danilo.altura)
