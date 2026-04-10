from turtle import *

tracer(0)
screensize(5000, 5000)
lt(90)
m = 20

for _ in range(2):
    forward(m * 21); rt(90); forward(m * 27); rt(90)

penup()
forward(m * 9); rt(90); forward(m * 10); lt(90)

pendown()
for _ in range(2):
    forward(m * 86); rt(90); forward(m * 47); rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()
#234