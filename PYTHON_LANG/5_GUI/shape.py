import turtle as t
import random

p = t.Turtle()
S = t.Screen()

colours = ["firebrick","dark violet","magenta","medium violet red","blue" ,"chartreuse"]
S.bgcolor("black")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        p.forward(50)
        p.right(angle)

for shape_side_n in range(3,21):
    p.color(random.choice(colours))
    draw_shape(shape_side_n)


S.exitonclick()
