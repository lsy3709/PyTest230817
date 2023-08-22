# 엑셀 파일 부분에서 읽기 쓰기
# 파일의 확장자 , xls, xlsx
# 터미널 창에서, pip install xlrd
# 각자 자리에 엑셀을 열수 있는 응용 프로그램.
# 리브레 오피스를 받아서 설치 해주기.
import xlrd

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 엑셀 파일 : 워크북
# 엑셀 파일의 구조 특성상, 하단에 탭 부분: 워크시트
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

# 워크북(엑셀파일)의 워크시트(탭부분 내용) 내용을 가지고 옴.
# junior, senior
wsheetList = workbook.sheets()
print(f"wsheetList 결과.: {wsheetList}")
for worksheet in wsheetList:
    print('** 워크시트의 이름 : %s' % (worksheet.name))
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
