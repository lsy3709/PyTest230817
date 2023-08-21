
num=int(input("숫자를 입력하세요:"))

print("입력하신 숫자는 %d 입니다"%num)

result=''
while (num>0):
    mind=num%2
    num=num//2
    result=str(mind)+result

print(result)