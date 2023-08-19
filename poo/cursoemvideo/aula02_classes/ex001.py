"""
O que é um objeto?
Coisa Material ou abstrata que pode ser percebida pelos sentidos e descrita
por meio das suas características (atributos), comportamentos (métodos) 
e estado(status) atual.
"""


class Caneta():
    """Docstring que defini o que a classe faz"""
    def __init__(self, modelo="Bic", cor="Azul", ponta="média"):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = 100
        self.tampada = True

    def rabiscar(self):
        if self.tampada:
            print('[ERRO] Impossível rabiscar com a caneta tampada')
        else:
            print('Rabiscando...')
            self.carga -= 1

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def estado(self):
        print(
            f'Caneta {self.cor}, modelo {self.modelo} com ponta {self.ponta}.')
        print(
            f'Sua carga atual é {self.carga}% e está {"tampada" if self.tampada else "destampada"}.')


c1 = Caneta()

c1.estado()

c1.rabiscar()
c1.estado()

c1.destampar()
c1.rabiscar()

c1.estado()
