inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

# 한번에 다 읽어서, 리스트에 담았고,
inList = inFp.readlines()
# 리스트에서 요소를 하나씩 꺼내서, 출력하는 부분.
for inStr in inList:
    print(inStr, end="")

inFp.close()
