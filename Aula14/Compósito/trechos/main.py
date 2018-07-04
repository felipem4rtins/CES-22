# Felipe Martins Gomes
# Comp 20
# Exercício: Padrão Compósito
# Programa compilado com PyCharm 2018.1.2


from trecho import Caminho
from trecho.trechos import Andando, Carro


def main():

    trecho1 = Andando(
        "Vá até o cruzamento da Rua H8C com a Av. Nossa Sra. de Loreto",
        50
    )

    trecho2 = Carro(
        "Vá até o cruzamento da Av. Nossa Sra. de Loreto com a Rua H8A",
        100
    )

    trecho3 = Carro(
        "Vire a direita na Rua H8A",
        50
    )

    caminho1 = Caminho()
    caminho1.adiciona(trecho1)
    caminho1.adiciona(trecho2)

    print("**** Caminho 01 ****")
    caminho1.imprime()

    caminho2 = Caminho()
    caminho2.adiciona(caminho1)
    caminho2.adiciona(trecho3)

    print("\n**** Caminho 02 ****")
    caminho2.imprime()


if __name__ == '__main__':
    main()
