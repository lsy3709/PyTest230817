# call by value 확인
def f(x):
    # y, x 지역변수 사용중
    # global x, 이미 전역으로 사용된 변수를 함수 내부에서 재선언이 안됨
    # 자바 스크림트로 치면 기존에는 var 변수타입으로 재선언 및 재할당 등이 가능하지만,
    # es6 버전 이후로는 let, const를 이용해서, 해당 블록 범위서 재선인 안되게 됨
    # 파이썬에서도 해당 블록 범위에서 전역으로 재선언을 막고 있다.
    y = x
    y = 3
    return y*y


# #전역 선언 및 할당
x = 3
print(f(x))
print(x)


# call by reference 확인
def spam(eggs):
    print(f"eggs의 id 확인: {id(eggs)}")
    eggs.append(1)  # ham의 리스트에 1을 추가하는 부분
    print(f"eggs의 id 확인2  원소 추가 후: {id(eggs)}")
    # 다른 레퍼런스 eggs 라는 지역 변수에 할당
    # eggs 효력 범위. 시작 끝으로 생명주기를 다함
    eggs = [2, 3]  # [2,3] 리스트이고 이것은 다른 인스턴스입니다.
    print(f"eggs의 id 확인3 다른 리스트의 메모리([2,3] 위치 주소값 할당 후): {id(eggs)}")


ham = [0]  # ham이라는 인스턴스
print(f"ham의 id 확인0 함수가 실행되기 전 인자 레퍼런스: {id(ham)}")
spam(ham)
print(ham)
print(f"ham의 id 확인1 함수가 실행된 후 인자 레퍼런스: {id(ham)}")


# call by value 확인
# def f(x):
#     y = x
#     x = 5
#     return y*y

# #전역 선언 및 할당
# x=3
# print(f(x))
# print(x)
