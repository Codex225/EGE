from turtle import *

m = 20
tracer(0)
screensize(5000, 5000)
rt(90)

penup()
bk(3 * m); rt(90); bk(15 * m); lt(90)
pendown()

for _ in range(2):
    fd(m * 10); rt(90); fd(m * 18); rt(90)

penup()
bk(m * 5); rt(90); fd(m * 7); lt(90)
pendown()

for _ in range(2):
    fd(m * 10); rt(90); fd(m * 7); rt(90)
penup()
goto(0, -50 * m)
pendown()
goto(0, 50 * m)

penup()
goto(-50 * m, 0)
pendown()
goto(50 * m, 0)

penup()
for x in range(0, 50):
    for y in range(0, 50):
        goto(x * m, y *m )
        dot(3, "red")

update()
done()

#85