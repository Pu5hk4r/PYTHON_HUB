import turtle as t
import random

p = t.Turtle()
screen = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r,g,b) #returning tuple
    return random_color



directions = [0,90,180,270] #East--->North-->West--->South
p.pensize(12)
p.speed("fastest")  #make the speed faster
screen.bgcolor("black")  #background color



for _ in range(500):
    p.color(random_color())
    p.forward(30)
    p.setheading(random.choice(directions))


screen.exitonclick()