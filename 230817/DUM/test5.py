
# 십진수 -> 이진수
print("숫자 입력 :")
decimal = int(input())
result = ''
print(f"십진수: {decimal}")
while(decimal>0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print(f"이진수: {result}")