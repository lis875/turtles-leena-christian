'''from turtle import *
for _ in range(5):
    forward(100)  # Move forward by 100 units
    right(144)    # Turn right by 144 degrees
done()
'''
from turtle import *

for _ in range(5):
    # Loop to draw a single star
    for _ in range(5):
        forward(100)  # Move forward by 100 units
        right(144)    # Turn right by 144 degrees
    
    # Move the turtle to the starting position for the next star
    penup()
    forward(150)  # Move forward to create space between stars
    pendown()
done()