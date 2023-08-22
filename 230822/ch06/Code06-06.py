<<<<<<< HEAD
import csv

# 주의: 단위 원이나 1000단위 단위로 콤마하는 부분 오류 해결
=======
# 주의 사항, 단위 원 1000 단위로 콤마를 하는 부분에 대해서 오류가 발생.

>>>>>>> 58d01b2e15c94c4afe3d49e5be64ec2cbced9a97
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
