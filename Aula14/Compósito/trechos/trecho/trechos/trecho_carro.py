from trecho.trecho import Trecho


class Carro(Trecho):

    def __init__(self, direcao, distancia):
        self.direcao = direcao
        self.distancia = distancia

    def imprime(self):
        print("\nVá de carro: ")
        print(self.direcao)
        print("A distância percorrida será de %d metros" % self.distancia)
