from plataforma.plataforma import Plataforma


class PS4(Plataforma):

    def __init__(self, mediator):
        super(PS4, self).__init__(mediator)

    def recebe_mensagem(self, mensagem):
        print("PS4 recebeu:", mensagem)
