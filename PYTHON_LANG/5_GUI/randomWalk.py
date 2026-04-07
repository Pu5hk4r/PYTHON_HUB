import turtle as t
import random

p = t.Turtle()
screen = t.Screen()

colours = ["firebrick","dark violet","cyan","saddle brown","blue" ,"chartreuse"]
directions = [0,90,180,270] #East--->North-->West--->South
p.pensize(12)
p.speed("fastest")
screen.bgcolor("black")



for _ in range(500):
    p.color(random.choice(colours))
    p.forward(30)
    p.setheading(random.choice(directions))


screen.exitonclick()