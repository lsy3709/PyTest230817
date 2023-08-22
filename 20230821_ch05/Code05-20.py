inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    # end="" 전체 출력 끝부분을 결정함
    print(inStr, end="")

inFp.close()
