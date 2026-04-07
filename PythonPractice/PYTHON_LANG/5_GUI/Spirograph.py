import turtle as t
import random

p = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r,g,b)
    return color

p.speed("fastest")
screen.bgcolor("black")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        p.color(random_color())
        p.circle(100)
        p.setheading(p.heading() + 10)

draw_spirograph(5)

screen.exitonclick()