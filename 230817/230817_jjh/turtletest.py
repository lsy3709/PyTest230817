import turtle
import random

## 함수 선언 부분 ##
## 반드시 들여쓰기 할 것 ##
def  screenLeftClick(x, y):
    # global 선언은 static과 유사함
    global r, g, b
    # turtle 인스턴스는 아래에서 초기화했을 것임
    # pencolor : 펜 색상 결정
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    # 해당 위치로 선을 그리면서 이동
    # pendown + goto

def  screenRightClick(x, y):
    global r, g, b
    # 해당 위치까지 선을 그리지 않고 이동
    # penup + goto
    turtle.penup()
    turtle.goto(x, y)

def  screenMidClick(x, y):
    global r, g, b
    # 1 ~ 10의 숫자 중 하나를 랜덤으로 선택
    tSize = random.randrange(1, 10)
    # 거북이 모양 크기
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    print(r, g, b, tSize)

def turtlefunc():
    global r, g, b

    for i in range(0, 10):
        tSize = random.randrange(1, 5)
        turtle.shapesize(tSize)
        turtle.pencolor(r, g, b)
        r = random.random()
        g = random.random()
        b = random.random()
        turtle.color(r, g, b)
        if i == 0:
            turtle.lt(36)
        else:
            if i % 2 == 0:
                turtle.lt(144)
            else:
                turtle.rt(72)
        turtle.pendown()
        turtle.forward(200)
        turtle.stamp()


## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.penup()
turtle.sety(-200)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtlefunc()

turtle.done()
