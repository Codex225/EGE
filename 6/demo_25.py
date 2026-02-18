from turtle import *

m = 30
screensize(5000, 5000)
tracer(0)
left(90)
for i in range(2):
    forward(14 * m); left(270), back(12 * m); right(90)
penup()
forward(9 * m); right(90); back(7 * m); left(90)
pendown()
for i in range(2):
    forward(m * 13); right(90); forward(m * 6); right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "red")
update()
done()
