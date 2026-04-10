from turtle import *

tracer(0)
screensize(5000, 5000)
m = 20
penup()
goto(m * 10, m * 15)
pendown()
lt(90)

for _ in range(15):
    for j in range(20):
        forward(m * 40); rt(90)
    lt(90)

penup()
for x in range(1, 50):
    for y in range(1, 55):
        goto(m * x, m * y)
        dot(3, "red")

update()
done()

#2544