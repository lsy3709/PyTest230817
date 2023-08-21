import turtle as t
import random

t.shape('turtle')

# t.bgcolor("black")

color = ("red", "orange", "blue", "green", "pink")

# t.speed(0)
# for x in range(20):
#     t.up()
#     t.goto(random.randint(-300, 300), random.randint(-300, 300))
#     t.down()

#별 그리기
t.color(random.choice(color))
t.begin_fill()

for i in range(5):
    t.forward(100)
    t.left(144)
t.end_fill()


#이름
t.color(random.choice(color))

t.hideturtle()
t.write("김도연", move=False, align="center", font=("arial", 50, "bold"))
t.penup()
t.sety(-100)
t.pendown

t.done()
