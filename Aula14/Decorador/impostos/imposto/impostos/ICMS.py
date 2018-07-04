from imposto.imposto import Imposto
from imposto.decorator import IPVX


class ICMS(Imposto):

    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)
