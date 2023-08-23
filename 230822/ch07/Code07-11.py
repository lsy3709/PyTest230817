# 컬러 이미지 파일 읽어서, 각 RGB 색을 추출 하는 부분.
#
from tkinter import *


window = Tk()
photo = PhotoImage(file='C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()
print('이미지 크기 : ', h, 'x', w)

# 컴프리헨션 파이썬 스타일 코드.
# 부교재 5단원,
# 결론, 리스트 안에 반복문을 통해서, 값을 설정.부분.
# 1) 리스트(밖에for) 안에 리스트 (안쪽  for ) 있다면, 뒤에(바깥 for문 )고정
# 2) 리스트 (밖에쪽  for )하나만 있다면, 앞에(바깥 for문 )고정
# 결과 : w x h 행렬 형식이다.
# 예) w:3, h: 5 -> [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]
# photoR = [[0 for _ in range(5)] for _ in range(3)]
# print(f"photoR 의 결과 : {photoR}")
photoR = [[0 for _ in range(h)] for _ in range(w)]
photoG = [[0 for _ in range(h)] for _ in range(w)]
photoB = [[0 for _ in range(h)] for _ in range(w)]

for i in range(w):
    for k in range(h):
        r, g, b = photo.get(i, k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

print('[50][50] 위치의 RGB 값 : ', photoR[50][50], photoG[50][50], photoB[50][50])
