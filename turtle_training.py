# import turtle module
import turtle

s = turtle.getscreen
turtle.title("Turtle Training Academy - You Gotta Train Your Turtle")
turtle.bgcolor("lavender")

# This variable name (t) is what we will call our turtle
t = turtle.Turtle()
# Appropriately shaped
t.shape("turtle")

t.pensize(5)
t.pencolor("white")
t.fillcolor("light blue")

# I turned certain things into functions to call upon later
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
    

def pick_pen_up():
    t.penup()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(125)

def circles_w_clone():
    t.begin_fill()
    t.circle(90)
    t.end_fill()

    # Our second turtle
    c = t.clone()
    c.circle(50)

def six_circles():
    n = 10 
    while n <= 60:
        t.circle(n)
        n = n + 10

x = input("Would you like me to draw you a shape? [y]es or [n]o: ")
if x == "y":
    circles_w_clone()
elif x == "n":
    print("Well, okay then.")
else:
    print("Hm? Invalid reply. Terminating program.")