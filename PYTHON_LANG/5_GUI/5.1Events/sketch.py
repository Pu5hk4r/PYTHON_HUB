from turtle import Turtle, Screen

p = Turtle()
sc =  Screen()

def move_forwards():
    p.forward(10)

def move_backwards():
    p.backward(10)

def turn_left():
    new_heading = p.heading() + 10
    p.setheading(new_heading)

def turn_right():
    new_heading = p.heading() - 10
    p.setheading(new_heading)

def clear():
    p.clear()
    p.penup()
    p.home()


sc.listen() #collect key events
sc.onkey(move_forwards, "w")
sc.onkey(move_backwards,"s")
sc.onkey(turn_left,"a")
sc.onkey(turn_right,"d")
sc.onkey(clear,"c")




sc.exitonclick()
