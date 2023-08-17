## 실습 3. 이진수 계산하기
x = int(input("이진수로 변환할 십진수를 입력하시오 : "))

binarylist = []

while True:
    binarylist.append(x % 2)
    x = x // 2
    if x == 1:
        binarylist.append(x)
        break

result = ""

#for i in reversed(range(len(binarylist))):
#    result += str(binarylist[i])

for i in range(len(binarylist) - 1, 0, -1):
    result += str(binarylist[i])
result += str(binarylist[0])

print(result)