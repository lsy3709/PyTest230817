import xlrd

# workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
workbook = xlrd.open_workbook(
    'C:/Users/it/Downloads/850131_DC750_market_sales_20230822110413.xls')
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

wsheetList = workbook.sheets()
print(f"wsheet: {wsheetList}")
for worksheet in wsheetList:
    print('** 워크시트의 이름 : %s' % (worksheet.name))
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
