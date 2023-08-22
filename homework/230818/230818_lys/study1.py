# call by reference 확인
def spam(eggs):
    print(f"eggs의 id 확인1: {id(eggs)}")
    eggs.append(1)  # ham 의 리스트에 1을 추가하는 부분         <- 추가해도 'ham'의 주소는 바뀌지 않기때문에 그대로 출력됨
    print(f"eggs의 id 확인2 원소 추가후: {id(eggs)}")
#     # 다른 레퍼런스 eggs 라는 지역 변수에 할당.
#     # eggs 효력 범위. 시작 끝으로 생명주기를 다함.
    eggs = [2, 3]  # [2,3] 리스트이고 이것은 다른 인스턴스입니다.            <- 지금까지 봤던건 spam(ham)에서   ham = [0,1] 의 주소였으나, 이건 그냥 eggs라는 새로운 리스트를 만든것 
    print(f"eggs의 id 확인3 다른 리스트의 메모리([2,3]) 위치주소값 할당 후: {id(eggs)}")


ham = [0]  # ham 이라는 인스턴스,
print(f"ham의 id 확인0 함수가 실행 전 인자 레퍼런스: {id(ham)}")
spam(ham)
print(ham)
print(f"ham의 id 확인4 함수가 실행 후 인자 레퍼런스: {id(ham)}")
