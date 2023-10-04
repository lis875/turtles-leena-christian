from turtle import *

def draw_star(color):
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(100)
        right(144)
    end_fill()

setup(600, 200)
speed(0)

star_colors = ["red", "green", "blue", "yellow", "orange"]

for color in star_colors:
    penup()
    forward(150) 
    pendown()
    draw_star(color)

done()
