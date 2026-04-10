from turtle import *

tracer(0)
screensize(5000, 5000)
lt(90)
m = 40

rt(30)
for _ in range(18):
    forward(m * 11); rt(120); forward(m * 11); rt(60)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()
#104
