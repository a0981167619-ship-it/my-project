import turtle
t=turtle.Turtle()
colors=["aliceblue","lightcyan","paleturquoise","skyblue","lightblue"]
t.pensize(3)
t.setheading(0)
for i in range(4):
    t.pencolor(colors[i%len(colors)])
    t.forward(40)
    t.right(125)
    t.forward(40)
    t.left(55)
t.forward(40)
t.right(125)
t.forward(48)
t.left(55)

for a in range(12):
    t.pencolor(colors[i%len(colors)])
    t.forward(40)
    t.right(125)
    t.forward(40)
    t.left(55)
    t.forward(40)
    t.right(125)
    t.forward(48)
    t.left(55)
    t.penup()
    t.right(120)
    t.pendown()
    t.pencolor(colors[a%len(colors)])
    t.forward(40)
    t.right(125)
    t.forward(40)
    t.left(55)
    t.forward(40)
    t.right(125)
    t.forward(48)
    t.left(55)


    


   



