# Felipe Martins Gomes
# Comp 20
# Exercício 3.8.11
# Programa compilado com PyCharm 2018.1.2


import turtle
janela = turtle.Screen()
felipe = turtle.Turtle()

felipe.left(72)
felipe.forward(100*(1+5**(1/2))/2)

for i in range(4):
    felipe.right(144)
    felipe.forward(100*(1+5**(1/2))/2)

janela.mainloop()
