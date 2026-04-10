from turtle import *

tracer(0)
screensize(5000,5000)
m = 20
lt(90)

for _ in range(2):
    forward(m * 23); lt(90); backward(m * 27); lt(90)

penup()
backward(m * 5); rt(90); forward(m * 11); lt(90)
pendown()

for _ in range(2):
    forward(m * 26); rt(90); forward(m * 32); rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()
tracer(0)
#1189