inFp, outFp = None, None
inStr = ""
# 문자열이 아닌 이진 값을 읽고 쓰기 예제.
# 바이너리 읽은 인스턴스
inFp = open("C:/Windows/write.exe", "rb")
# 바이너리 쓰는 인스턴스.
outFp = open("C:/Temp/write.exe", "wb")

# 계속 파일의 내용을 없을 때까지 계속 쓰기.
while True:
    # 읽는 인스턴스에서 1바이트 씩 읽어서.
    inStr = inFp.read(1)
    # 없으면 반복문 빠저나가고
    if not inStr:
        break
    # 그렇지 않다면, 내용이 있다면, 바이너리로 쓰기 작업.
    outFp.write(inStr)

inFp.close()
outFp.close()
print("--- 이진 파일이 정상적으로 복사되었음 ---")
