# Felipe Martins Gomes
# Comp 20
# Exercício 3.8.6
# Programa compilado com PyCharm 2018.1.2


import turtle
janela = turtle.Screen()
felipe = turtle.Turtle()

for i in range(3):
    felipe.forward(50)
    felipe.left(120)

felipe.penup()
felipe.forward(100)
felipe.pendown()

for i in range(4):
    felipe.forward(50)
    felipe.left(90)

felipe.penup()
felipe.forward(100)
felipe.pendown()

for i in range(6):
    felipe.forward(50)
    felipe.left(60)

felipe.penup()
felipe.forward(125)
felipe.pendown()

for i in range(8):
    felipe.forward(50)
    felipe.left(45)

janela.mainloop()