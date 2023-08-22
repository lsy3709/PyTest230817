import csv

# 주의: 단위 원이나 1000단위 단위로 콤마하는 부분 오류 해결
with open("C:/CookAnalysis/CSV/singer2.csv", "r") as inFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    print(header_list[1], header_list[6])
    for inStr in inFp:
        inStr = inStr.strip()
        row_list = inStr.split(',')
        youtube = int(row_list[6])
        youtube = int(youtube/10000)
        print(row_list[0], str(youtube)+"만")
