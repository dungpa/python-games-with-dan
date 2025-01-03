import turtle
from itertools import cycle
from random import randint

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
backgrounds = cycle(['dark red', 'dark orange', 'dark goldenrod', 'dark green', 'dark blue', 'dark violet'])

def draw_shape(size, angle, shift):
    turtle.bgcolor(next(backgrounds))
    turtle.pensize(randint(1, 25))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size + 5, angle + 1, shift + 1)

turtle.bgcolor('black')
turtle.speed('fast')
draw_shape(30, 0, 1)
