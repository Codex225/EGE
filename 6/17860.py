from turtle import *

tracer(0)
screensize(5000, 5000)
m = 20
left(90)

for _ in range(9):
    forward(m * 22); right(90); forward(m * 6); right(90)
penup()
forward(m * 1); right(90); forward(m * 5); left(90)
pendown()

for _ in range(9):
    forward(m * 53); right(90); forward(m * 75); right(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()