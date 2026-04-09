from turtle import *

tracer(0)
screensize(5000, 5000)
m = 20
lt(90)

for _ in range(9):
    fd(m * 22); rt(90); fd(m * 6); rt(90)

penup()
fd(m * 1); rt(90); fd(m * 5); lt(90)
pendown()

for _ in range(9):
    fd(m * 53); rt(90); fd(m * 75); rt(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")
update()
done()
