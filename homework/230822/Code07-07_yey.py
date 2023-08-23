# 2개의 csv를 합쳐서, 엑셀 파일에 출력
# 최종 n개의 csv를 합쳐서, 한방에 엑셀 파일에 출력
import xlwt
import csv
# os : 운영체제의 절대경로, path 를 제공
import os

# csv 재료 합치려는 csv 파일명 목록
csvFileList = ["C:/CookAnalysis/Excel/a01.csv", "C:/CookAnalysis/Excel/c01.csv", "C:/CookAnalysis/Excel/b01.csv"]
# xlwt 엑셀 파일 만드는 인스턴스
outWorkbook = xlwt.Workbook()

# csv 경로의 파일명을 가지고 온다
for csvFileName in csvFileList :
    # 임시 카운트 목적의 상태 변수
    # 해더를 제외한 실제 데이터를 분리하기 위한 값
    rowCount = 0
    # csvFileName : csv 파일의 절대 경로 위치
    # inFp, 인스턴스 임시 저장
    with open(csvFileName, "r") as inFp:
        # 다시, csv 모듈의 reader 함수를 이용
        csvReader = csv.reader(inFp)
        # next 함수 이용해서, 한 행을 불러옴
        # 보통 첫번째 행은 컬럼을 의미
        header_list = next(csvReader)
        # 새 엑셀 파일 -> 워크 시트이름 작성하는 함수
        print(f"os.path.basename(csvFileName)의 값 : {os.path.basename(csvFileName)}")
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        # 헤더의 컬럼의 갯수, 데이터의 컬럼의 갯수 동일
        for col in range(len(header_list)) :
            # 엑셀 파일의 각 셀의 위치에 값을 쓰는 부분
            outSheet.write(rowCount, col, header_list[col])
        # csv 파일의 내용을 각행의 정보를 불러옴
        for row_list in csvReader:
            # 실제 데이터 부분은 2번째 행부터라서 값 증가
            rowCount += 1
            # row_list : 실제 데이터의 행의 size, len 길이는 컬럼의 갯수의미
            for col in range(len(row_list)):
                # 조건은 해당 값이 숫자이면, 
                if row_list[col].isnumeric() :
                    # 엑셀 파일에 쓰겠다. 실수형으로
                    outSheet.write(rowCount, col, float(row_list[col]))
                else :
                    # 숫자가 아니면 그냥 쓰겠다.
                    outSheet.write(rowCount, col, row_list[col])

outWorkbook.save('c:/CookAnalysis/Excel/abc01_0822.xls')
print("Save. OK~")