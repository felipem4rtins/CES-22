# Felipe Martins Gomes
# Comp 20
# Exercício 7.26.12
# Programa compilado com PyCharm 2018.1.2


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

janela = fazer_janela("white", "casa")
felipe = fazer_turtle("black", 8)

movimento = [(90, 100), (90, 100), (90, 100), (135, 100*2**0.5), (90, 50*2**0.5),
             (90, 50*2**0.5), (90, 100*2**0.5), (225, 100)]

for (x, y) in movimento:
    fazer_movimento(felipe, x, y)

janela.mainloop()