import turtle
import random


def  screenLeftClick(x, y):
    
    namedraw()    


# 이름 그리는 함수
def namedraw() :    

    turtle.penup()
    turtle.goto(-300, 100)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    
    turtle.setx(-200)
    turtle.sety(200)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(110)
    turtle.penup()

    turtle.setx(-200)
    turtle.sety(180)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()

    turtle.setx(-200)
    turtle.sety(140)
    turtle.left(0)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()

    turtle.setx(-230)
    turtle.sety(10)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()

    

def  screenRightClick(x, y):    # 우클릭시 기능
    turtle.penup()              # 선을 안그리고 이동
    turtle.goto(x, y)           # x, y로 이동

def  screenMidClick(x, y):              # 휠 클릭시
    global r, g, b                      
    tSize = random.randrange(1, 10)     # tSize : 정수값 1~9까지 랜덤한 정수 선택
    turtle.shapesize(tSize)             # 거북이 모양 크기 : shapesize
    # r, g, b 0~255 사이값 할당
    r = random.random()
    g = random.random()
    b = random.random()

    print(f"랜덤한 색상의 값 : r = {r} , g = {g}, b = {b}")


## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('arrow')
turtle.pensize(pSize)

# 이벤트 헨들러 역할
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
