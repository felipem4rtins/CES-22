def IPVX(calcula):

    def wrapper(self, orcamento):
        return calcula(self, orcamento) + 50.0

    return wrapper
