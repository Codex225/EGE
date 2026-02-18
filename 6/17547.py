from turtle import *

screensize(5000, 5000)
left(90)
m = 30
tracer(0)
for i in range(3):
    forward(7 * m); right(90); forward(12 * m); right(90)
penup()
forward(4 * m); right(90); forward(6 * m); left(90)
pendown()
for i in range(4):
    forward(83 * m); right(90); forward(77 * m); right(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "red")

update()
done()
