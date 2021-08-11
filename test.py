from turtle import *
import random
speed(0)
x = random.randint(-200,170)
y = random.randint(-200,170)
for i in range(0, 100):
    if x<0 and y<0:
        color("red")
    elif x<0 and y>0:
      color("green")
    elif x>0 and y>0:
      color("blue")
    else:
      color("yellow")
    begin_fill()
    for j in range(0, 4):
        forward(30)
        right(90)
        penup()
        goto(x,y)
    end_fill()