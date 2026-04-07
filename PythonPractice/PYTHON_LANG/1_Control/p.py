import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics Example")

# Create a turtle named "pen"
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)  # Move forward by 100 units
    pen.right(90)     # Turn right by 90 degrees

# Close the window when clicked
screen.exitonclick()
