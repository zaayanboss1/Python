import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
p=turtle.Turtle()
sides=6
length=70
angle=360/sides
for i in range(sides):
    p.forward(length)
    p.right(angle)
turtle.done()