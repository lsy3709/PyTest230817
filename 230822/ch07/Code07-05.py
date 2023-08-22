import xlrd
import xlwt

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
outWorkbook = xlwt.Workbook()
idx = 4  # 평균 키의 인덱스

wsheetList = workbook.sheets()
outSheet = outWorkbook.add_sheet("singer")
worksheet = wsheetList[0]
for col in range(worksheet.ncols):
    # 0행부터 시작해서 열(col)부분만 값을 쓰기
    outSheet.write(0, col, worksheet.cell_value(0, col))

totalRow = 0
for worksheet in wsheetList:
    for row in range(1, worksheet.nrows):
        # 평균키를 의미하는 인덱스의 값을 가져와서 각열에 대해서 키가 165 이상이면 아래 실행
        height = worksheet.cell_value(row, idx)
        if int(height) >= 165:
            totalRow += 1
            for col in range(worksheet.ncols):
                outSheet.write(totalRow, col, worksheet.cell_value(row, col))

outWorkbook.save('c:/CookAnalysis/Excel/outSinger2.xls')
print("Save. OK~")
