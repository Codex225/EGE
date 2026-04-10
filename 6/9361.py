from turtle import *

tracer(0)
screensize(5000, 5000)
m = 30
lt(90)
penup()
goto(-m * 3, -m * 4)
pendown()

rt(90)
for _ in range(10):
    fd(m * 14); rt(120)

penup()
for x in range(-50, 0):
    for y in range(-50, 0):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#4