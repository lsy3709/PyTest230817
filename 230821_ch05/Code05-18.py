inFp = None  # 입력 파일
inStr = ""		# 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8")
# inFp = open("C:/Temp/data1.txt", "r")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    # end="" , 전체 출력 끝부분에 정하는 옵션.공백이라서 아무것도 없음.
    #
    print(inStr, end="!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

inFp.close()
