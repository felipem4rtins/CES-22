# Felipe Martins Gomes
# Comp 20
# Exercício 3.8.12
# Programa compilado com PyCharm 2018.1.2


import turtle
janela = turtle.Screen()
janela.bgcolor("lightgreen")
felipe = turtle.Turtle()
felipe.shape("turtle")
felipe.color("blue")

felipe.stamp()
felipe.left(90)
felipe.penup()
felipe.forward(100)
felipe.pendown()
felipe.forward(10)
felipe.penup()
felipe.forward(10)
felipe.pendown()
felipe.stamp()
felipe.right(180)
felipe.penup()
felipe.forward(120)
felipe.pendown()
felipe.left(150)

for i in range(11):
    felipe.penup()
    felipe.forward(100)
    felipe.pendown()
    felipe.forward(10)
    felipe.penup()
    felipe.forward(10)
    felipe.pendown()
    felipe.stamp()
    felipe.right(180)
    felipe.penup()
    felipe.forward(120)
    felipe.pendown()
    felipe.left(150)

felipe.right(90)

janela.mainloop()

