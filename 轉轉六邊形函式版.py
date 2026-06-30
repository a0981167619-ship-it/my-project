import turtle
t=turtle.Turtle()
def cvinn_fght(size):
    t.pensize(3)
    t.speed(10)
    t.penup()
    t.goto(0,0)
    t.pendown()
    side_length=10
    colors=["#7BE38D","#9BF2A9","#BDF8C8","#DFFFE6"]
    for a in range(6):
        t.pencolor(colors[a%len(colors)])
        t.left(60)
        t.forward(50)
        for i in range(size):
            length=side_length*(i+1)
            t.forward(length)
            t.left(60)
cvinn_fght(10)
turtle.done()
        
    
