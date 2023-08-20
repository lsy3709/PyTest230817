import turtle as t
import random

n = 60    # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
t.hideturtle()

t.write("조경제", move=False, align="center", font=("arial",50,"bold"))
def setcolor():
    global r,g,b
    r = random.random()
    g = random.random()
    b = random.random()
    
r, g, b = 0.0, 0.0, 0.0
def draw(): 
    for i in range(n):
        setcolor()
        t.circle(120)       # 반지름이 120인 원을 그림
        t.right(360 / n)    # 오른쪽으로 6도 회전

for i in range(10):
    t.pencolor(0.0,0.0,0.0)
    t.forward(200)
    setcolor()
    t.left(60)
    draw()


t.done()
