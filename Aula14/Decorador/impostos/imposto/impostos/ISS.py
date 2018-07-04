from imposto.imposto import Imposto
from imposto.decorator import IPVX


class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)
