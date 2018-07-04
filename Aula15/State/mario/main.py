# Felipe Martins Gomes
# Comp 20
# Exercício: Padrão State
# Programa compilado com PyCharm 2018.1.2


from mario import Mario


def main():

    mario = Mario()
    mario.pega_cogumelo()
    mario.pega_pena()
    mario.leva_dano()
    mario.pega_flor()
    mario.pega_flor()
    mario.leva_dano()
    mario.leva_dano()
    mario.pega_pena()
    mario.leva_dano()
    mario.leva_dano()
    mario.leva_dano()


if __name__ == '__main__':
    main()
