## 실습 1. 구구단 계산하기
x = int(input("구구단 몇 단을 계산할까 ? : "))

print("구구단 %d단을 계산한다" %(x))

for i in range(1, 10):
    print("%d x %d = %d" %(x, i, x * i))