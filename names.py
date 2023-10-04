import turtle

# Function to draw a red box around the text
def draw_red_box(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

# Set up the Turtle screen
turtle.setup(400, 200)
turtle.speed(0)  # Set the drawing speed (0 = fastest)

# Write your name
turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.write("Christian Willis", font=("Arial", 12, "normal"))

# Draw a red box around your name
#draw_red_box(45, 95, 130, 20)

# Write your partner's name
#turtle.penup()
#turtle.goto(50, 50)
#turtle.pendown()
#turtle.write("Leena", font=("Arial", 12, "normal"))

# Draw a red box around your partner's name
#draw_red_box(45, 45, 40, 20)

# Close the Turtle graphics window when clicked
turtle.exitonclick()
