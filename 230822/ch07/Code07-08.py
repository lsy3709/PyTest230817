# 엑셀 파일 -> csv 파일 쓰기.
import xlrd
import csv

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')

# 찾을 컬럼
findColumn = ['이름', '주소', '유튜브 조회수']
# 해당 컬럼 인덱스
findIndex = []

# 엑셀 파일의 워크시트
wsheetList = workbook.sheets()
# 첫번째 워크시트
worksheet = wsheetList[0]
# 첫번째 워크시트의 첫행 : 헤더
header_list = worksheet.row_values(0)

# findColumn = ['이름', '주소', '유튜브 조회수']
for name in findColumn:
    # 예) 이름, 주소, 유튜브 조회수에 대한 각 인덱스 모두 조회.
    findIndex.append(header_list.index(name))

# 엑셀의 워크시트 목록
wsheetList = workbook.sheets()
# csv 파일에 쓰기 위한 인스턴스, 자동 메모리 반납 포함. with ~ as
with open("C:/CookAnalysis/Excel/singer_youtube_230822.csv", "w", newline='') as outFp:
    # csv 모듈의 writer 이용해서 쉽게 쓰기 기능 구현.
    csvWriter = csv.writer(outFp)
    # 첫행 헤더를 쓰는 부분.
    csvWriter.writerow(findColumn)
    # 2번째 행, 실제 데이터를 입력 하는 부분.
    for worksheet in wsheetList:
        # 엑셀의 전체 행의  갯수, 보통 구조가 동일해서,
        # 1행의 크기는 , 다른 행의 크기와 보통 다 동일함.
        for row in range(1, worksheet.nrows):
            # 임시 리스트
            findList = []
            # 엑셀의 열의 크기 만큼 반복.
            for col in range(worksheet.ncols):
                # 이름, 주소, 유튜브 조회수 여기에 포함이 되면 값을 추가.
                if col in findIndex:
                    # 임시 리스트에 추가하고,
                    findList.append(worksheet.row_values(row)[col])
            # 실제 csv 파일에 쓰기 작업.
            csvWriter.writerow(findList)

print("Save. OK~")
