<<<<<<< HEAD
=======

# 엑셀 파일 읽어서 ->csv 출력.

>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
import xlrd
import csv

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')

wsheetList = workbook.sheets()
for worksheet in wsheetList:
<<<<<<< HEAD
    with open("C:/CookAnalysis/Excel/singer_" + worksheet.name + "230822.csv", "w", newline='') as outFp:
        csvWriter = csv.writer(outFp)
        for row in range(worksheet.nrows):
            row_list = worksheet.row_values(row)
=======
    # 지정된 경로의 파일에 csv로 쓰기 작업.
    with open("C:/CookAnalysis/Excel/singer_" + worksheet.name + "230822.csv", "w", newline='') as outFp:
        # outFp : csv 파일에 쓰기위한 인스턴스
        # csv 모듈의writer 함수 이용해서 쉽게 쓰기 작업 진행중.
        csvWriter = csv.writer(outFp)

        #
        for row in range(worksheet.nrows):
            print(f"row 의 값: {row}")
            row_list = worksheet.row_values(row)
            print(f"row_list 의 값: {row_list}")
>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
            csvWriter.writerow(row_list)

print("Save. OK~")
