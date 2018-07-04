from plataforma.mediator import Mediator
from plataforma.plataformas.ps4 import PS4
from plataforma.plataformas.wiiu import WiiU


class MensagemMediator(Mediator):

    def __init__(self):
        self.contatos = []

    def adiciona(self, plataforma):
        self.contatos.append(plataforma)

    def envia(self, mensagem, plataforma):
        for contato in self.contatos:
            if (contato != plataforma):
                self.__definir_protocolo(contato)
                contato.recebe_mensagem(mensagem)

    def __definir_protocolo(self, contato):
        if (type(contato) == type(PS4)):
            print("Protocolo PS4")
        elif (type(contato) == type(WiiU)):
            print("Protocolo WiiU")
