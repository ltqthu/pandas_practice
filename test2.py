from turtle import *
color("purple")  # 定义画笔颜色
pensize(5)    # 定义画笔的线条的宽度
speed(10)    # 定义绘图的速度
penup()   # 抬起画笔
goto(300, 250)   # 以0,0为起点进行绘制
pendown()     # 落下画笔
# 绘出正方形的四条边
for i in range(4):
    forward(50)
    right(90)