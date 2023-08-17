
import turtle
import random


def  screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
   
    r = random.random()
    g = random.random()
    b = random.random()



    turtle.left(30)
    turtle.forward(100)
    turtle.right((360/n)*2)
    turtle.forward(100)
    turtle.left(360/n)
    

    turtle.pendown()
    turtle.goto(x, y)
    turtle.color(r,g,b)

def  screenRightClick(x, y):

   
    for i in range(0, 5):
        
        turtle.forward(100)
        turtle.left(144)

def screenMixClick(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.clear()
    turtle.write("지은")

# def turnRight():
#     turtle.setheading(0)
#     turtle.forward(50)

# def turnUp():
#     turtle.setheading(90)
#     turtle.forward(50)

# def turnLeft():
   
#     turtle.setheading(180)
#     turtle.forward(50)

# def turnDown():

#     turtle.setheading(270)
#     turtle.forward(50)

def blank():
    turtle.clear

pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 실습')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMixClick,2)
turtle.onscreenclick(screenRightClick, 3)


# turtle.onkeypress(turnRight,"Right")
# turtle.onkeypress(turnLeft,"Left")
# turtle.onkeypress(turnUp,"UP")
# turtle.onkeypress(turnDown,"DOWN")
# turtle.onkeypress(blank,"Escape")
# turtle.listen()
turtle.done()
