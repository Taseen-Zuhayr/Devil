import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)
pencil = turtle.Turtle()
for i in range(3):
    pencil.forward(100)
    pencil.left(120)
pencil.penup()
pencil.left(90)
pencil.forward(50)
pencil.pendown()
pencil.right(90)
for i in range(3):
    pencil.forward(100)
    pencil.right(120)


turtle.done()
