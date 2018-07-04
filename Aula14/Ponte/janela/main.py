# Felipe Martins Gomes
# Comp 20
# Exercício: Padrão Ponte
# Programa compilado com PyCharm 2018.1.2


from janela.concreta import JanelaMac, JanelaLinux, JanelaWindows
from janela.abstrata import JanelaDialogo, JanelaAviso


def main():

    janela = JanelaDialogo(JanelaLinux())
    janela.desenhar()
    print()

    janela = JanelaAviso(JanelaLinux())
    janela.desenhar()
    print()

    janela = JanelaDialogo(JanelaWindows())
    janela.desenhar()
    print()

    janela = JanelaAviso(JanelaMac())
    janela.desenhar()


if __name__ == '__main__':
    main()
