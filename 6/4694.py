from turtle import *

m = 30
screensize(5000, 5000)
tracer(0)
lt(90)
for i in range(7):
    forward(10 * m); right(120)

up()
for x in range(-50, 50):
    for y in range (-50, 50):
        goto(x * m,y * m)
        dot(3, "red")

update()
done()