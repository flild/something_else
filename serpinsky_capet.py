from turtle import * 
import random
import time
    
setup(width=1920, height=1080, startx=0, starty=0)
bgcolor("black")
speed(9)
color('white')
pensize(1)

points = [[-200, 0], [0, 200], [200, 0]]
penup()
goto(-200, 0)
pendown() 
dot()

penup()
goto(0, 200)
pendown()
dot()

penup()
goto(200, 0)
pendown()
dot()

penup()
x, y = random.randint(-200, 200), random.randint(0, 200)
goto(x, y)
pendown()
dot()
for i in range(10000):
    R = random.random()
    G = random.random()
    B = random.random()
    color(R, G, B)
    point = random.choice(points)
    x = x + (point[0] - x)/2
    y = y + (point[1] - y)/2
    penup()
    goto(x, y)
    pendown()
    dot()
mainloop()