from turtle import *

tracer(0)
screensize(5000, 5000)
lt(90)
m = 30

for _ in range(4):
    forward(m * 12); lt(90)
penup()
rt(270)
back(m * -7)
lt(180)
pendown()

for _ in range(4):
    forward(m * 8); rt(270)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#30
