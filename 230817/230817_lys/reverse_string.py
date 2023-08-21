b=""

while True:
    a=input("문자열을 입력하세요(0 입력시 종료) : ") 
    
    for i in range(len(a)-1,-1,-1):
       b=b+a[i]                                   

    print(f"역순 : {b}")

    if a==0:
        break

print("종료")
    