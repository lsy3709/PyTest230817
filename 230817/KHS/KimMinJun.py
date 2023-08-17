# 브랜치 테스트

import turtle as t

# t.shape('turtle')
# t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
# for i in range(300):    # 300번 반복
#     t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
#     t.right(91)         # 오른쪽으로 91도 회전

t.bgcolor("black")
t.color("pink")
t.speed(5)  # 1(가장느림)~10(빠름) 0:최고속도

for i in range(200):
    t.pensize(i/50)
    t.forward(i)
    t.left(65)

t.color("Lightblue")
t.setheading(270)

for i in range(50):
    t.pensize(25 - i/2)
    t.forward(i/4)
