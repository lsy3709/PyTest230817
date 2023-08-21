outFp = None
outStr = ""

# w, r 이라든지, b가 빠져 있으면, 기본은 모드 텍스트 모드
# 이미지 처럼, 문자가 아닌 이진값을 읽을 때는
# 모드 b 붙음
# 예) 쓰기 작업시 : bw
# 예) 읽기 작업시 : rw
outFp = open("C:/Temp/data2.txt", "w")

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")
