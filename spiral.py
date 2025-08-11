import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(300,400)
p=turtle.Turtle()
size=0
while True:
    for i in range(4):
        p.fd(size+1)
        p.left(90)
        size=size-5
    size=size+1