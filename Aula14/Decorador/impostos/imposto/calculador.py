class CalculadorDeImpostos(object):

    def realize_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print("Calculo:", imposto_calculado)
