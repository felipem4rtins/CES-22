# Felipe Martins Gomes
# Comp 20
# Exercício 7.26.13
# Programa compilado com PyCharm 2018.1.2


import turtle

import turtle

def fazer_janela (cor, titulo):
    janela = turtle.Screen()
    janela.bgcolor(cor)
    janela.title(titulo)
    return janela

def fazer_turtle (cor, tamanho):
    tartaruga = turtle.Turtle()
    tartaruga.color(cor)
    tartaruga.pensize(tamanho)
    return tartaruga

def fazer_movimento (tartaruga, x, y):
    tartaruga.left(x)
    tartaruga.forward(y)

def desenhar_figura (tartaruga, x, y):
    tartaruga.left(x)
    tartaruga.forward(y)

janela = fazer_janela("white", "casas")
felipe = fazer_turtle("black", 8)

#felipe.left(90)
#felipe.penup()
#felipe.forward(300)
#felipe.right(90)
#felipe.pendown()

movimento1 = [(270, 100), (90, 100), (90, 100), (45, 50*2**0.5), (90, 50*2**0.5), (135, 100)]

for (x,y) in movimento1:
    desenhar_figura(felipe, x, y)

felipe.penup()
felipe.forward(130)
felipe.pendown()

movimento2 = [(270, 100), (270, 100), (270, 100), (315, 50*2**0.5), (270, 50*2**0.5),
             (225, 100), (135, 100*2**0.5)]

for (x,y) in movimento2:
    desenhar_figura(felipe, x, y)

felipe.penup()
felipe.left(90)
felipe.forward(100)
felipe.left(45)
felipe.pendown()

movimento3 = [(225, -50*2**0.5), (270, -100*2**0.5), (270, -100*2**0.5), (270, -50*2**0.5),
              (315, -100), (270, -100), (270, -100), (270, -100)]

for (x,y) in movimento3:
    desenhar_figura(felipe, x, y)

felipe.penup()
felipe.right(45)
felipe.forward(240)
felipe.pendown()
felipe.left(180)

movimento4 = [(90, -50*2**0.5), (90, -100*2**0.5), (90, -50*2**0.5), (135, -100), (270, -100),
              (315, -50*2**0.5), (270, -50*2**0.5), (225, -100), (135, -100*2**0.5), (135, -100),
              (135, -100*2**0.5)]

for (x,y) in movimento4:
    desenhar_figura(felipe, x, y)

janela.mainloop()