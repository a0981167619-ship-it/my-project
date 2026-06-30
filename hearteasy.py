import turtle
t=turtle.Turtle()
t.pensize(4)
colors=["lightpink","pink","lavenderblush","hotpink","deeppink"]
for i in range(10):
    t.pencolor(colors[i%len(colors)])
    t.left(45)
    t.forward(50)
    t.circle(30,180)
    t.penup()
    t.goto(0,0)
    t.right(80)
    t.pendown()
    t.forward(50)
    t.circle(-30,180)

    t.penup()
    t.goto(0,0)


