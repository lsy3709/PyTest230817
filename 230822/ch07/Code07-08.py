import xlrd
import csv

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')

findColumn = ['이름', '주소', '유튜브 조회수']
findIndex = []

wsheetList = workbook.sheets()
worksheet = wsheetList[0]
header_list = worksheet.row_values(0)
for name in findColumn :
    findIndex.append(header_list.index(name))

wsheetList = workbook.sheets()
with open("C:/CookAnalysis/Excel/singer_youtube.csv", "w", newline='') as outFp:
    csvWriter = csv.writer(outFp)
    csvWriter.writerow(findColumn)
    for worksheet in wsheetList :
        for row in range(1, worksheet.nrows) :
            findList = []
            for col in range(worksheet.ncols) :
                if col in findIndex :
                    findList.append(worksheet.row_values(row)[col])
            csvWriter.writerow(findList)

print("Save. OK~")