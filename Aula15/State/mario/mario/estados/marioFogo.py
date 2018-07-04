from mario.marioState import MarioState, Estado


class MarioFogo(MarioState):

    def pega_cogumelo(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioGrande')
        return mario.pega_estado()

    def pega_flor(self):
        print("Mario ganhou 1000 pontos")
        mario = Estado('MarioFogo')
        return mario.pega_estado()

    def pega_pena(self):
        print("Mario ganhou pena e pode voar")
        mario = Estado('MarioCapa')
        return mario.pega_estado()

    def leva_dano(self):
        print("Mario foi morto")
        mario = Estado('MarioMorto')
        return mario.pega_estado()
