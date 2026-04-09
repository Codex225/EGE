from turtle import *

m = 20
tracer(0)
screensize(5000, 5000)
lt(90)

for _ in range(2):
    fd(m * 24); rt(90); fd(m * 10); rt(90)

fd(m * 3); lt(90); fd(m * 13); rt(90)

for _ in range(2):
    fd(m * 9); rt(90); fd(m * 32); rt(90)

penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")
update()
done()

#120