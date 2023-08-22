print("구구단 몇 단을 계산할까요?")

x = 1

while (x is not 0):
    x = int(input())
    if x == 0:break
    if not(1 <= x <= 9):
        print("재입력", "1~9")
        continue
    else:
        print("구구단" + str(x) + "단을 계산합니다.")
        for i in range(1,10):
            print(str(x) + "X" + str(i) + "=" + str(x*i))
        print("구구단 몇 단을 계산할까요?")
print("종료")