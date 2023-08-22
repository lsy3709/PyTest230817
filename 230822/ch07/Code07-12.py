
# 이미지의 각 픽셀의 RGB 의 값을
# 각 워크시트 이름으로 : R, G, B 워크 시트 3개
# 각 셀의 0~ 255 의 값을 할당.
from tkinter import *
import xlsxwriter
window = Tk()
# PhotoImage , 이미지 절대 경로의 파일을 읽어서, 인스턴스에 임시 저장.
photo = PhotoImage(file='C:/CookAnalysis/GIF/pic7.gif')
# photo 에 이미지의 정보가 들어 있어서, 높이 , 폭을 구할수 있음.
# 각 RGB의 이중 리스트의 , 규격이 될 예정.
h = photo.height()
w = photo.width()

# 컴프리헨션이라는 표현으로, 파이썬 스타일의 코드
# 리스트 안에 반복문으로 통해서, 빈 이중 리스트를 만든다.
photoR = [[0 for _ in range(h)] for _ in range(w)]
photoG = [[0 for _ in range(h)] for _ in range(w)]
photoB = [[0 for _ in range(h)] for _ in range(w)]

#
for i in range(w):
    for k in range(h):
        # 언패킹 해당 위치의 rgb 값을 각 변수에 풀어서 할당.
        # photo 이미지의 정보를 가지고 있고,
        # get 함수를 이용해서, 해당 픽섹 위치의 RGB 값을 재할당.
        r, g, b = photo.get(i, k)
        # 각 비어있는 이중 리스트에 값을 할당.
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

# 엑셀 파일의 각 워크시트에 , 값을 쓰는 기능.
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/pic7_230822.xlsx')
worksheetR = workbook.add_worksheet('photoR')
worksheetG = workbook.add_worksheet('photoG')
worksheetB = workbook.add_worksheet('photoB')

# 각 워크시트에서 내용을 채우는 부분.
for i in range(w):
    for k in range(h):
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

workbook.close()
print('Save. OK~')
