inFp = None
inList = ""

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

# readlines , 한번에 다 읽기.
inList = inFp.readlines()
print(inList)

inFp.close()
