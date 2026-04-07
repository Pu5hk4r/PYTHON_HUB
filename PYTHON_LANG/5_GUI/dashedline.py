from turtle import Turtle,Screen
p= Turtle()


# p.forward(100)
# p.back(200)
# p.right(-90)
# p.forward(250)
# p.left(90)
# p.forward(100)
# p.setpos(50,-70)

for _ in range(15):
    p.forward(10)
    p.penup() #stop drawing line
    p.forward(10)
    p.pendown()




screen = Screen()
screen.exitonclick()