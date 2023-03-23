# import turtle module
import turtle

s = turtle.getscreen
turtle.title("Turtle Training Academy - You Gotta Train Your Turtle")
turtle.bgcolor("lavender")

t = turtle.Turtle()
t.shape("turtle")

t.pensize(5)
t.pencolor("white")
t.fillcolor("light blue")

# I turned ceertain things into functions to call upon later
# as opposed to deleting the code when not in use.
def myshape():
    t.right(90)
    t.forward(100)
    t.left(90)
    t.backward(100)

    t.goto(100, 100)
    t.home()

def rectangle():
    t.fd(200)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(100)
    t.end_fill()

def pick_pen_up():
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(125)


t.begin_fill()
t.circle(90)
t.end_fill()

c = t.clone()
c.circle(50)
