import csv
import glob
import os
import xlwt

file_list = glob.glob(os.path.join('C:/CookAnalysis/CSV/csvs/', '*.csv'))
firstYN = True

outputXls = xlwt.Workbook()
print(file_list)
for input_csv in file_list:
    if firstYN == True:
        outCount = 0
    else:
        outCount = 1
    with open(input_csv, 'r') as nowcsv:
        myworkbook = csv.reader(nowcsv)
        headerlist = next(myworkbook)
        if firstYN == True:
            output = outputXls.add_sheet(os.path.basename(input_csv))
            for col in range(len(headerlist)):
                print(headerlist[col])
                output.write(outCount, col, headerlist[col])
            outCount += 1
            firstYN = False
        for datalist in myworkbook:
            for col in range(len(datalist)):
                print(datalist[col], outCount)
                output.write(outCount, col, datalist[col])
            outCount += 1
    firstYN = True
    
outputXls.save("c:/CookAnalysis/Excel/fish_total_data_230822.xls")

        
    # nowworksheet = myworkbook
    # with open("C:/CookAnalysis/Excel/fishdataMerging.xls", "a", newline='') as outFp:
    #     mycsvwriter = csv.writer(outFp)
    #     if firstYN == True:
    #         headerlist = []
    #         for col in range(1, nowworksheet.max_column + 1):
    #             headerlist.append(nowworksheet.cell(row = 1, column = col).value)
    #         mycsvwriter.writerow(headerlist)
    #         firstYN = False
    #     for row in range(2, nowworksheet.max_row + 1):
    #         datalist = []
    #         for col in range(1, nowworksheet.max_column + 1):
    #             datalist.append(nowworksheet.cell(row = row, column = col).value)
    #         mycsvwriter.writerow(datalist)

print("csv merging is completed !!!!!!!")
