import xlwt
import csv
import os

csvFileList = ["C:\CookAnalysis\CSV\강원인구통합.csv",
               "C:\CookAnalysis\CSV\강원도_인구추이 통계_20191231.csv"]
outWorkbook = xlwt.Workbook()

for csvFileName in csvFileList:
    rowCount = 0
    with open(csvFileName, "r") as inFp:
        csvReader = csv.reader(inFp)
        header_list = next(csvReader)
        outSheet = outWorkbook.add_sheet(os.path.basename(csvFileName))
        for col in range(len(header_list)):
            outSheet.write(rowCount, col, header_list[col])
        for row_list in csvReader:
            rowCount += 1
            for col in range(len(row_list)):
                if row_list[col].isnumeric():
                    outSheet.write(rowCount, col, float(row_list[col]))
                else:
                    outSheet.write(rowCount, col, row_list[col])

outWorkbook.save(
    'C:/PyTest2023/PyTest230817/homework/230822_smlee/smlee230822_gangwon_statistics_CSV.xls')
print("Save. OK~")
