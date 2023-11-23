import turtle

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(100)


t.penup()
t.goto(0,-50)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-60)
t.pendown()
t.circle(60)
t.penup()
t.goto(0,-200)
t.pendown()
t.circle(200)
t.penup()
t.goto(0, -210)
t.pendown()
t.circle(210)
t.penup()

for i in range(36):
    t.forward(100)
    t.pendown()
    t.forward(10)
    t.penup
    t.goto(0,0)
    t.pendown()
    t.left(10)
    