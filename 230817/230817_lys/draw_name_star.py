import turtle as t



def drawname(x,y):
    t.setheading(-90)
    
    #이
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(x+150,y+90)
    t.pendown()
    t.forward(220)

    #영
    t.penup()
    t.goto(x+200,y+20)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(x+300,y+40)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.penup()
    t.goto(x+300,y+10)
    t.pendown()
    t.forward(50)
    t.penup()
    t.goto(x+350,y+90)
    t.pendown()
    t.right(90)
    t.forward(130) 
    t.penup()
    t.goto(x+270,y-100)
    t.pendown()
    t.circle(40)

    #석
    t.penup()
    t.goto(x+450,y+65)
    t.pendown()
    t.right(35)
    t.forward(90)
    t.back(50)
    t.left(80)
    t.forward(60)
    t.penup()
    t.goto(x+470,y+30)
    t.pendown()
    t.setheading(0)
    t.forward(50)
    t.penup()
    t.goto(x+520,y+90)
    t.pendown()
    t.setheading(-90)
    t.forward(130)
    t.penup()
    t.goto(x+440,y-60)
    t.pendown()
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.penup()

def drawstar(x,y):
    t.setheading(-108)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.forward(144)
        t.left(144)
    t.penup()


def screenLeftClick(x, y):
    drawname(x,y)

def screenRightClick(x,y):
    drawstar(x,y)

t.speed(0)
t.pensize(8)
t.onscreenclick(screenLeftClick, 1)
t.onscreenclick(screenRightClick, 3)
t.done()