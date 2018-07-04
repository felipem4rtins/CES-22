# Felipe Martins Gomes
# Comp 20
# Exercício: Padrão Mediador
# Programa compilado com PyCharm 2018.1.2


from plataforma import MensagemMediator
from plataforma.plataformas import PS4, WiiU


def main():

    mediator = MensagemMediator()

    wiiu = WiiU(mediator)
    ps4 = PS4(mediator)

    mediator.adiciona(wiiu)
    mediator.adiciona(ps4)

    wiiu.envia_mensagem("Oi, eu sou da Nintendo!")
    ps4.envia_mensagem("Olá, eu sou da Sony!")


if __name__ == '__main__':
    main()
