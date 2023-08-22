<<<<<<< HEAD
from tkinter import *
# csv 파일을 읽고 화면에 출력하기
# 함수 선언 부
# 빈 시트를 만들기
=======
# 파이썬 버전의, GUI , 윈도우 창에, 특정 라벨(UI)
# 임시 데이터 내용을 화면에 표시하기.
from tkinter import *

# 함수 선언 부
# 빈 테이블을 만들기.
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97


def makeEmptySheet(r, w):
    retList = []
    for i in range(0, r):
        tmpList = []
        for k in range(0, w):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList


# 전역 변수부
csvList = [['제목1', '제목2', '제목3'],
           [111, 222, 333],
           [444, 555, 666],
           [777, 888, 999]]
rowNum, colNum = 4, 3
workSheet = []

# 메인 코드부
window = Tk()
<<<<<<< HEAD
=======
# 빈 테이블 만들기
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
workSheet = makeEmptySheet(rowNum, colNum)

# 워크시트에 리스트값 채우기. (= 각 빈 셀에 값 넣기)
for i in range(0, rowNum):
    for k in range(0, colNum):
        workSheet[i][k].insert(0, csvList[i][k])

window.mainloop()
