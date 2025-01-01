import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    
t.penup()
t.speed('slow')
t.bgcolor('Light salmon')

# feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# legs
t.goto(-25, -50)
rectangle(15, 100, 'navy')
t.goto(-55, -50)
rectangle(-15, 100, 'navy')

#body
t.goto(-90, 100)
rectangle(100, 150, 'medium blue')

# arms
t.goto(-150, 70)
rectangle(60, 15, 'navy')
t.goto(-150, 110)
rectangle(15, 40, 'navy')

# hands
t.goto(-155, 130)
rectangle(25, 25, 'deep sky blue')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'deep sky blue')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())

t.goto(10, 70)
rectangle(60, 15, 'navy')
t.goto(55, 110)
rectangle(15, 40, 'navy')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'navy')

# head
t.goto(-85, 170)
rectangle(80, 50, 'medium blue')

# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 160)
rectangle(5, 5, 'black')
t.goto(-45, 157)
rectangle(5, 5, 'black')

# mouth
t.goto(-65, 135)
t.right(9)
rectangle(40, 5, 'black')

# antennae
t.left(9)
t.goto(-85, 220)
rectangle(5, 60, 'midnight blue')

t.goto(-95, 230)
rectangle(20, 20, 'yellow')

t.goto(-45, 220)
rectangle(5, 60, 'midnight blue')

t.goto(-55, 230)
rectangle(20, 20, 'yellow')

t.goto(-10, 220)
rectangle(5, 60, 'midnight blue')

t.goto(-20, 230)
rectangle(20, 20, 'yellow')

t.hideturtle()
