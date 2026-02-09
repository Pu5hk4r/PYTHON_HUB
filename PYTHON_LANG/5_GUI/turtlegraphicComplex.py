import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Create the turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)  # Fastest drawing speed

# Colors to use in the drawing
colors = ["red", "yellow", "blue", "green", "purple", "orange", "cyan", "magenta"]

# Function to draw a spiral pattern
def draw_spiral():
    for i in range(360):
        pen.pencolor(colors[i % len(colors)])  # Change color in a cyclic manner
        pen.width(i // 100 + 1)  # Increase the width as we go
        pen.forward(i * 3 / 2 + i)  # Move the turtle forward with a growing distance
        pen.left(59)  # Turn the turtle

# Function to draw nested shapes
def draw_shapes():
    for i in range(36):
        draw_spiral()  # Draw the spiral pattern
        pen.right(10)  # Rotate the entire pattern by a small angle

# Starting position
pen.penup()
pen.setpos(-200, 100)
pen.pendown()

# Draw the complex pattern
draw_shapes()

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
