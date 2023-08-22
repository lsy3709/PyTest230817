import xlrd

<<<<<<< HEAD
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
sheetCount = workbook.nsheets

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            print("%s" % worksheet.cell_value(row, col), end = '\t')
        print()
    print()
=======
# 엑셀 파일 읽기, workbook 인스턴스 , 메모리 임시로 저장.
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# workbook nsheets 속성을 이용해서 값을 구함.
sheetCount = workbook.nsheets

# 워크시트의 이름 목록.
wsheetList = workbook.sheets()
# 각 워크 시트의 이름, 행 , 열 조회.
# 반복문으로 , 읽어서, 터미널에 출력을 하고 있음.
for worksheet in wsheetList:
    print('** 워크시트의 이름 : %s' % (worksheet.name))
    for row in range(worksheet.nrows):
        for col in range(worksheet.ncols):
            print("%s" % worksheet.cell_value(row, col), end='\t')
        print()
    print()
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
