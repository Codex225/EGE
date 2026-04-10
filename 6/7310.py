from turtle import *

tracer(0)
screensize(5000, 5000)
m = 20
lt(90)

for _ in range(4):
    forward(m * 10), rt(90)

penup()
fd(m * 3); lt(90); fd(m * 5); rt(90)
pendown()

for _ in range(2):
    fd(m * 10); rt(90); fd(m * 12); rt(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#171