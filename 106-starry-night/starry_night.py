import turtle as t
from random import randint, random

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
    
# Main code
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow', 0, 0)

while True:
    ran_pts = randint(2, 5) * 2 + 1
    ran_size = randint(10, 50)
    ran_col = (random(), random(), random())
    ran_x = randint(-350, 300)
    ran_y = randint(-250, 250)
       
    draw_star(ran_pts, ran_size, ran_col, ran_x, ran_y)