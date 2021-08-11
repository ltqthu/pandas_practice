from turtle import *
import random
speed(0)
x = random.randint(-200,170)
y = random.randint(-200,170)
for i in range(0, 100):
    x = random.randint(-200,170)
    y = random.randint(-200,170)
    penup()
    goto(x,y)
    if x<0:
        color("red")
    else:
      color("yellow")
    # begin_fill()
    for j in range(0, 4):
        forward(30)
        right(90)
    # end_fill()