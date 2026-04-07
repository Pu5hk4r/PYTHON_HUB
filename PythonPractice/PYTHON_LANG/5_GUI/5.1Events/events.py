from turtle import Turtle, Screen

from PIL.ImageChops import screen

p = Turtle()
sc =  Screen()

def move_forwards():
    p.forward(10)

sc.listen() #collect key events
sc.onkey(key="space",fun=move_forwards) #register key events ,no need for parenthesis as its high order function




sc.exitonclick()
