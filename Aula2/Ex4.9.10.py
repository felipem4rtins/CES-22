# Felipe Martins Gomes
# Comp 20
# Exercício 4.9.10
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

def desenhar_estrelas (tartaruga, tamanho):
    for i in range(5):
        desenhar_estrela(tartaruga, tamanho)
        tartaruga.penup()
        tartaruga.forward(350)
        tartaruga.right(144)
        tartaruga.pendown()

janela = fazer_janela("lightgreen", "5 estrelas")
felipe = fazer_turtle("pink", 3)
desenhar_estrelas(felipe, 100)

janela.mainloop()