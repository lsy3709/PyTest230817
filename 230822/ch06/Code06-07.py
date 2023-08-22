import csv

with open("C:/CookAnalysis/CSV/singer2.csv", "r") as inFp :
    csvReader = csv.reader(inFp)
    header_list = next(csvReader)
    print(header_list[1],header_list[6])
    for row_list in csvReader:
        youtube = int(row_list[6].replace(',',''))
        youtube = int(youtube/10000)
        print(row_list[1], str(youtube)+"만")