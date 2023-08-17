

num=int(input("구구단 몇단을 계산할까? :"))

print("구구단 %d단을 계산합니다!"%num)


for i in range(10):
    print("%d x %d= %d" %(num,i,num*i))

    