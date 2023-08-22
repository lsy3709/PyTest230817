import openpyxl

workbook = openpyxl.load_workbook('c:/CookAnalysis/Excel/singer.xlsx')
wsheetList = workbook.sheetnames

for wsName in wsheetList :
    worksheet = workbook[wsName]
    print('** 워크시트의 이름 : %s' % (wsName) )
    for row in range(1, worksheet.max_row+1) :
        for col in range(1, worksheet.max_column+1) :
            print("%s" % (worksheet.cell(row=row, column=col).value), end='\t')
        print()
    print()