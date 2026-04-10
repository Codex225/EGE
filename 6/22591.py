from turtle import *

tracer(0)
screensize(5000, 5000)
lt(90)
m = 10

for _ in range(4):
    fd(m * 50); lt(90)

penup()
fd(m * 50), lt(135)
pendown()

for _ in range(2):
    fd(m * 102); lt(120); fd(m * 182); lt(60)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#1250