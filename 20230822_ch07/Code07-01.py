import xlrd
# 터미널 창에서 ,pip install xlrd

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 엑셀 파일 : 워크북
# 엑셀 파일 구조 특성상 하단에 탭 부분 :워크시트
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

wsheetList = workbook.sheets()
print(f"원크시트 내용 : {wsheetList}")
for worksheet in wsheetList:
    print('** 워크시트의 이름 : %s' % (worksheet.name))
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
