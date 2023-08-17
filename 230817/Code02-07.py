# 파이썬 모듈 기반 형식(라이브러리= 도구 모음집)
import turtle
import random

# 실습
# !
# 왼쪽 클릭시 기능 추가.
# !
# 현재 기능
# 1) 색설정 & 선 그리면서 & 해당 좌표 이동.
# 추가
# a) 거북이 크기 변경 부분
# b) stamp 기능
# c) 회전 기능.
# d) 거북이 색깔 랜덤하게 변경.
# e) 선 색 랜덤하게 변경.

# 실습)
# 1. 터틀 함수 이용해서, 자기 이름도 그려보고,
# 2. 추가- 별 그려보기. 등. 친해지기. 재미 붙이기.


## 함수 선언 부분 ##
# 들여쓰기. 파이썬. 의무.


def screenLeftClick(x, y):

    # global 전역, static 비슷.
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    # 터틀 컬러
    # turtle.color('red')
    turtle.color(r, g, b)

    # turtle 인스턴스 초기화는 아래에서 진행 했을 것임.
    # pencolor ,매개변수 rgb 값을 받아서, 선색
    turtle.pencolor((r, g, b))
    # pendown , 선을 그리겠다 의미.
    turtle.pendown()

    # 크기 변경하기. 1)
    tSize = random.randrange(1, 10)
    # shapesize , 거북이 모양 크기.
    turtle.shapesize(tSize)

    # 거북이 도장 찍기.  2)
    turtle.stamp()

    # goto 매개변수 좌표값으로 이동.
    turtle.goto(x, y)

    # 거북이 회전, left , right
    turtle.left(random.randrange(1, 360))

# 우클릭시 , 기능.


def screenRightClick(x, y):
    # penup, 선을 안그리고
    turtle.penup()
    # 해당 좌표로 이동 x,y
    turtle.goto(x, y)

# 휠 클릭시.


def screenMidClick(x, y):
    # 전역으로 설정된 rgb 색깔 선언부분
    global r, g, b
    # 1~9 까지 랜덤한 정수 선택.
    tSize = random.randrange(1, 10)
    # shapesize , 거북이 모양 크기.
    turtle.shapesize(tSize)
    # 색상 랜덤을 이용해서, 할당. rgb, 0~255 사이의 값을 할당.
    r = random.random()
    g = random.random()
    b = random.random()
    print(f"랜덤한 색상의 값 조회: 0~255 , r : {r}, g : {g}, b : {b}")


## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

# 이벤트 핸들러 역할. onscreenclick
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
