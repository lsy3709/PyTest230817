import xlrd
# 추가 모듈 설치 : pip install xlwt
# 엑셀 파일 쓰기 용도.
# xlrd 읽기 용도.
import xlwt

# 엑셀 읽기.
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 엑셀 쓰기
outWorkbook = xlwt.Workbook()

# 엑셀 워크시트 이름 목록
wsheetList = workbook.sheets()
# 워크시트에서 각 하나의 워크시트 선택.
for worksheet in wsheetList:
    # 새 엑셀 파일에 -> 워크시트 이름을 추가하는 부분.
    outSheet = outWorkbook.add_sheet(worksheet.name)
    # 읽은 엑셀 파일의 전체 행의 갯수
    for row in range(worksheet.nrows):
        # 읽은 엑셀 파일의 전체 열의 갯수
        for col in range(worksheet.ncols):
            # 새 엑셀 파일의 새 워크시트 부분의 이름 : outSheet
            # 첫 번째, 두번째 매개변수는 해당 셀의 위치이고,
            # 세번째 매개변수는 입력 값(읽은 엑셀 파일의 내용)
            outSheet.write(row, col, worksheet.cell_value(row, col))

# 실제 엑셀 파일에 저장 하는 함수.
outWorkbook.save('c:/CookAnalysis/Excel/outSinger1_230822.xls')
print("Save. OK~")
