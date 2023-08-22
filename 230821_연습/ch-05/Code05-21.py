outFp = None
outStr = ""

# w 쓰기, r 읽기 모드. 디폴트는 텍스트 모드
outFp = open("C:/Temp/data2.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")
