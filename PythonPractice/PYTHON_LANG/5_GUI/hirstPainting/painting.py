# import colorgram
#
# rgb_colors  = []
# colors = colorgram.extract('photo.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

p = t.Turtle()
s = t.Screen()
t.colormode(255)
p.speed("fastest")
p.penup() #only position move not draw anything
p.hideturtle()

color_list = [(213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

p.setheading(225)
p.forward(300)
p.setheading(0)
number_of_dots = 100


for dot_count  in range(1, number_of_dots + 1):
    p.dot(20, random.choice(color_list))
    p.forward(50)

    if dot_count % 10 == 0:
        p.setheading(90)
        p.forward(50)
        p.setheading(180)
        p.forward(500)
        p.setheading(0)





s.exitonclick()