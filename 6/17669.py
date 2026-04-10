from turtle import *

screensize(5000, 5000)
m = 20
lt(90)
tracer(0)

for _ in range(4):
    forward(m * 19); rt(90); forward(m * 30); rt(90)

penup()
forward(m * 2); rt(90); forward(m * 8); left(90)
pendown()

for _ in range(4):
    forward(m * 93); rt(90); forward(m * 97); rt(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#374