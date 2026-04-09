from turtle import *

tracer(0)
m = 20
screensize(5000, 5000)
lt(90)

for _ in range(3):
    pendown()
    for j in range(2):

        fd(m * 7); rt(90); fd(m * 7); rt(90)
    penup()
    fd(m * 6); rt(90); fd(m * 6); lt(90)


penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()
#76