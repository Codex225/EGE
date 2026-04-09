from turtle import *

tracer(0)
screensize(5000, 5000)
m = 20
lt(90)

for i in range(8):
    fd(16 * m); rt(90); fd(22 * m); rt(90)

penup()

fd(5 * m); rt(90); fd(5 * m); lt(90)

pendown()


for i in range(8):
    fd(52 * m); rt(90); fd(77 * m); rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m , y * m)
        dot(3, "red")


update()
done()

#187