from trecho.trecho import Trecho


class Caminho(Trecho):

    def __init__(self):
        self.caminho = []

    def adiciona(self, trecho):
        self.caminho.append(trecho)

    def remove(self, trecho):
        self.caminho.remove(trecho)

    def imprime(self):
        for trecho in self.caminho:
            trecho.imprime()
