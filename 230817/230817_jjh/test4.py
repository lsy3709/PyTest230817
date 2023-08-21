## 실습 2. 문자열 역순

x = input("역순으로 출력할 문자열을 입력하시오 : ")

count = len(x) - 1

resultstr = ""

while True:
    resultstr += x[count]
    count -= 1
    if count == -1:
        break

print(resultstr)