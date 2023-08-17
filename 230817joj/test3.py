print("원하는 구구단 입력 : ")
num = input()
for i in range(10):
    result = int(num)*i
    print(f"{num} X {i} = {result}")

print("=====================================================")
sentence = "I Love U"
reverse =''
for i in sentence:
    reverse = i+reverse

print(reverse)

print("=====================================================")


print("0보다 큰 10진수를 2진수로 변환 숫자를 입력하세요 : ")
num1 = int(input())
result =''
while(num1>=1):
    num2 = num1%2
    num1 = num1//2 
    result = str(num2)+result 
print(result)