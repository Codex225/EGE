from turtle import *

screensize(5000, 5000)
m = 20
lt(90)
tracer(0)

for x in range(4):
    fd(m * 16); lt(90); fd(20 * m); lt(90)

penup()

fd(4 * m); lt(90); fd(8 *m); rt(180)

pendown()

for x in range(3):
    fd(m * 35); lt(90); fd(6 * m); lt(90)

penup()

for x in range(- 50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "red")
update()
done()

#126