import turtle as t 

t.shape("turtle")
t.bgcolor("black")
t.pensize(10)
t.fillcolor('red')
t.pencolor('orange')
t.speed(5)

polygon = int(t.numinput("다각형", "숫자"))

t.begin_fill()
for i in range(polygon):
    t.forward(100)
    t.left(360/polygon)
t.end_fill()

t.exitonclick()