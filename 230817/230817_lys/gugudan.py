while True:
    a=int(input("구구단의 몇 단을 출력할까요?(0 입력시 종료) : "))

    for i in range(1,10,1):
        print(f"{a} X {i} = {a*i}")

    if a==0:
        break

print("종료")