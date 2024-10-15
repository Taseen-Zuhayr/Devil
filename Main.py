import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(1000,600)
pencil = turtle.Turtle()
for i in range(3):
    pencil.forward(300)
    pencil.left(120)
pencil.penup()
pencil.left(90)
pencil.forward(150)
pencil.pendown()
pencil.right(90)
for i in range(3):
    pencil.forward(300)
    pencil.right(120)


turtle.done()
