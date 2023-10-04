
"""from turtle import *

name = textinput("Name","Enter your name here: ")

write(name)

penup()
right(90)
forward(50)
left(90)
pendown()

name2 = textinput("Second Name", "Enter Second name here: ")

write(name2)

penup()
right(90)
forward(50)
left(90)
pendown()

done()
"""

from turtle import *

while True:
    name = textinput("Name", "Enter a name (or 'exit' to quit): ")
    
    if name.lower() == 'exit':
        break

    write(name, align="center", font=("Arial", 12, "normal"))

    penup()
    forward(45)
    pendown()
done()