from tkinter import *

## 함수 선언 부
def makeEmptySheet(r, w) :
    retList = []
    for i in range(0, r):
        tmpList = []
        for k in range(0, w):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수부
csvList = [ [ '제목1', '제목2' , '제목3'],
            [ 111, 222, 333],
            [ 444, 555, 666],
            [ 777, 888, 999]     ]
rowNum, colNum = 4, 3
workSheet = []

## 메인 코드부
window = Tk()
workSheet = makeEmptySheet(rowNum, colNum)

# 워크시트에 리스트값 채우기. (= 각 빈 셀에 값 넣기)
for i in range(0, rowNum) :
    for k in range(0, colNum) :
        workSheet[i][k].insert(0, csvList[i][k])

window.mainloop()