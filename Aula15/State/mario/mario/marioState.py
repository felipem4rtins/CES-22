from abc import ABC, abstractmethod


class MarioState(ABC):

    @abstractmethod
    def pega_cogumelo(self):
        pass

    @abstractmethod
    def pega_flor(self):
        pass

    @abstractmethod
    def pega_pena(self):
        pass

    @abstractmethod
    def leva_dano(self):
        pass


class Estado(object):

    def __init__(self, estado):

        if estado == 'MarioPequeno':
            from mario.estados.marioPequeno import MarioPequeno
        elif estado == 'MarioCapa':
            from mario.estados.marioCapa import MarioCapa
        elif estado == 'MarioGrande':
            from mario.estados.marioGrande import MarioGrande
        elif estado == 'MarioFogo':
            from mario.estados.marioFogo import MarioFogo
        else:
            from mario.estados.marioMorto import MarioMorto
        self.__estado = eval(estado)()

    def pega_estado(self):
        return self.__estado
