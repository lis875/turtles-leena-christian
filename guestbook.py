from turtle import *
from turtle import textinput

# Ask the user for the first name
name1 = textinput("Name 1", "Please enter the first name:")

# Ask the user for the second name
name2 = textinput("Name 2", "Please enter the second name:")

# Initialize the Turtle graphics window
setup(400, 200)
speed(0)

# Display the first name on the screen
penup()
goto(0, 0)
pendown()
write(f"Welcome, {name1}!", align="center", font=("Arial", 16, "normal"))

# Move the pen down
penup()
goto(0, -30)
pendown()

# Display the second name below the first one
write(f"Welcome, {name2}!", align="center", font=("Arial", 16, "normal"))

# Display a "Thank you" message below the second name
penup()
goto(0, -60)
pendown()
write("Thank you for visiting our guestbook.", align="center", font=("Arial", 12, "normal"))

# Close the Turtle graphics window when clicked
done()
