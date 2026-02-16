from turtle import *

screensize(5000, 5000)
left(90)
tracer(0)
m = 20

for i in range(2):
    forward(m * 10); right(90); forward(m * 20); right(90)
penup()
forward(m * 3); right(90); forward(m * 5); left(90)
pendown()
for i in range(2):
    forward(m * 70); right(90); forward(m * 80); right(90)
penup()
for x in range(100):
    for y in range(100):

        goto(x * m, y * m)
        dot(3, "red")
#update()
done()
