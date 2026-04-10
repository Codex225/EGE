from turtle import *

tracer(0)
screensize(5000, 5000)
m = 30
lt(90)

for _ in range(4):
    forward(m * 16); rt(90); forward(m * 18); rt(90)

penup()
rt(90); forward(m * 10); lt(90); forward(m * 10)
pendown()

for _ in range(4):
    forward(m * 15); rt(90)
penup()

forward(m * 1); lt(90); forward(m * 1); rt(90)
pendown()

for _ in range(7):
    forward(m * 12); rt(90)
penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m *x, m * y)
        dot(3, "red")

update()
done()

#54