
import turtle as t

t.shape('turtle')
t.bgcolor("black")
t.color("black")

n = 50
t.color("white")
t.speed(1)

t.up()
t.goto(-100,100)
t.color("green")
t.down()
t.goto(100,100)
t.up()
t.goto(0,100)

t.color("red")
t.goto(-60,-100)
t.down()
t.circle(50)
t.up()
t.goto(60,-100)
t.down()
t.circle(50)

# t.up()
# t.left(90)
# t.forward(100)
# t.right(90)

# for i in range(1):

#    t.down()

#    for i in range(n):
#       t.circle(80)
#       t.right(10)
#       t.forward(10)
    
#    t.up()

#    for i in range(n):
#       t.circle(50)
#       t.left(10)
#       t.forward(20)

#    t.down()

#    for i in range(n):
#       t.circle(80)
#       t.right(10)
#       t.forward(10)


t.done()