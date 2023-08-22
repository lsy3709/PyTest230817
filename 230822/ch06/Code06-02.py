# 파일 , 입력 또는 출력을 위한 인스턴스를 사용 후, 반납(메모리)
# with ~ as 구문은, 자동으로 해당 인스턴스를 반납.
# 자바9 with ~ resource 구문에서, 자동 autoClosable 인터페이스를 구현
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp:

    inStr = inFp.readline()
    print(inStr, end="")

    inStr = inFp.readline()
    print(inStr, end="")
