# Felipe Martins Gomes
# Comp 20
# Exercício 4.9.9
# Programa compilado com PyCharm 2018.1.2


import turtle

def fazer_janela (cor, titulo):
    janela = turtle.Screen()
    janela.bgcolor(cor)
    janela.title(titulo)
    return janela

def desenhar_estrela (tartaruga, tamanho):
    for i in range(5):
        tartaruga.forward(tamanho)
        tartaruga.right(144)

def fazer_turtle (cor, tamanho):
    tartaruga = turtle.Turtle()
    tartaruga.color(cor)
    tartaruga.pensize(tamanho)
    return tartaruga

janela = fazer_janela("white", "estrela")
felipe = fazer_turtle("black", 3)
desenhar_estrela(felipe, 100)

janela.mainloop()