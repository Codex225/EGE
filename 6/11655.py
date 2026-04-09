from turtle import *

screensize(5000, 5000)
tracer(0)
lt(90)
m = 30

for i in range(2):
    fd(m * 6); rt(90); fd(12 * m);  rt(90)

penup()

bk(3 *m ); lt(90); fd(5 * m); rt(90)

pendown()

for i in range(4):
    fd(m * 6); rt(90)

penup()
fd(8 *m)
pendown()

for i in range(4):
    fd(m * 8); rt(90)

#164


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, "red")

update()
done()