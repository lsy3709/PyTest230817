
def DecimalToBinary(x):
    q=""
    while True:
        a=x//2
        b=x%2
        q=q+str(b)
        x=a
        if(a==0):
            break
   
    r=""
    for i in range(len(q)-1,-1,-1):
        r=r+q[i]

    print(f"결과 : {r}")

def BinaryToDecimal(x):

    sum=0
    c=0
    for i in range(len(x)-1,-1,-1):
        sum=sum+(2**c)*int(x[i])
        c=c+1

    print(f"결과 : {sum}")





print("10진수 -> 2진수  : 0")
print(" 2진수 -> 10진수 : 1")

q=input("동작을 입력하세요 : ")


if(q=='0'):
    w=int(input("2진수로 변경할 10진수 : "))
    DecimalToBinary(w)
elif(q=='1'):
    w=input("10진수로 변경할 2진수 : ")
    BinaryToDecimal(w)