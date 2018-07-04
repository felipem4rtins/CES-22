# Felipe Martins Gomes
# Comp 20
# Exercício: Padrão Decorador
# Programa compilado com PyCharm 2018.1.2


from imposto.impostos.ISS import ISS
from imposto.impostos.ICMS import ICMS
from imposto.calculador import CalculadorDeImpostos
from imposto.orcamento import Orcamento


def main():

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(1000)

    calculador.realize_calculo(orcamento, ISS())
    calculador.realize_calculo(orcamento, ICMS())
    calculador.realize_calculo(orcamento, ISS(ICMS()))
    calculador.realize_calculo(orcamento, ISS(ICMS(ISS())))


if __name__ == '__main__':
    main()
