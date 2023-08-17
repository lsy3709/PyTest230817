# print("hello python!!!!!!!!!!!!@@@@@@@@@!")
# a=1
# b=5
# c="4"
# print(type(a))
# print(type(c))
# print(f"test a출력:{a}")
# print(a+b)

# print("출력형식 %d " %(a))


# print("이메일 입력을 해주세요")
# email=input()
# print(f"입력된 이메일:{email}")

import turtle as t
import random


# def screenRightClick(x,y):
#   # 펜을 들고 이동
#     turtle.penup()
#     # 해당 좌표로 이동
#     turtle.goto(x,y)

# def screenLeftClick(x,y):
#     global r,g,b
#     r=random.random()
#     g=random.random()
#     b=random.random()
    

#     turtle.color(r,g,b)
#     turtle.pencolor((r,g,b))
#     turtle.pendown()

#     # 1~9까지 랜덤정수
#     tSize=random.randrange(1,10)
#     # shapsize 거북이 모양 크기
#     turtle.shapesize(tSize)

#     turtle.stamp()
#     turtle.goto(x,y)
#     turtle.left(random.randrange(1,360))

# pSize=10
# r,g,b=0.0,0.0,0.0




# turtle.title('거북이로 그림 그리기')
# turtle.shape('turtle')
# turtle.pensize(pSize) 

count = 0

while True:
  global r,g,b
  r = random.random()
  g = random.random()
  b = random.random()

  t.speed(0)
  if(count==4):
    for i in range(100):
      t.forward(i)
      t.left(144)
      t.pencolor((r, g, b))

   
    count=0
  else:
    count+=1
    
    


turtle.done()

