from tkinter import *
import csv
## 함수 선언 부
def makeEmptySheet(r, w) :
    retList = []
    for i in range(0, rowNum):
        tmpList = []
        for k in range(0, colNum):
            ent = Entry(window, text='', width=10)
            ent.grid(row=i, column=k)
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

## 전역 변수부
csvList = []
rowNum, colNum = 0, 0
workSheet = []

## 메인 코드부
window = Tk()

with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)
    csvList.append(header_list)
    for row_list in csvReader:
        csvList.append(row_list)

rowNum = len(csvList)
colNum = len(csvList[0])
workSheet = makeEmptySheet(rowNum, colNum)

idx = 6 # 평균 키의 인덱스
for i in range(0, rowNum) : # 워크시트에 리스트값 채우기. (= 각 빈 셀에 값 넣기)
    for k in range(0, colNum) :
        if ( csvList[i][idx].isnumeric() ) :
            if ( int(csvList[i][idx]) >= 167) :
                ent = workSheet[i][k]
                ent.configure(bg='yellow')
        workSheet[i][k].insert(0, csvList[i][k])

window.mainloop()