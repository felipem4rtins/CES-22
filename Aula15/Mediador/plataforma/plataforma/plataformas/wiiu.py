from plataforma.plataforma import Plataforma


class WiiU(Plataforma):

    def __init__(self, mediator):
        super(WiiU, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):
        print("WiiU recebeu:", mensagem)
