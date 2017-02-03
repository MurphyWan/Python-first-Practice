import turtle

def draw_K(k):
    k.left(90)
    k.forward(70.72)
    k.goto(0, 0)
    k.right(45)
    k.forward(100)
    k.goto(0, 0)
    k.right(90)
    k.forward(100)
    k.goto(0,0)
    k.right(45)
    k.forward(70.72)
    k.goto(0,0)
    
        
def draw_C(c):
    c.pu()
    c.setx(70.72 + 35.36)
    c.sety(70.72)
    c.pd()
    c.left(90)
    c.forward(70.72)
    c.goto(70.72 + 35.36, 70.72)
    c.right(90)
    c.forward(70.72*2)
    c.left(90)
    c.forward(70.72)


def Turtle_Mini_Project_KC():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)

    draw_K(brad)
    draw_C(brad)
    
    window.exitonclick()


Turtle_Mini_Project_KC()
