import turtle as t
from random import randint, random

t.shape('turtle')
t.speed('fastest')

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
    
def draw_planet(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
# Main code
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow', 0, 0)

while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(25, 75)
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
       
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
    
    ranCol = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)
       
    draw_planet(ranCol, ranX, ranY)
