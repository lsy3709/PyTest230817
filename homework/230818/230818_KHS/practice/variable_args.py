def b(*args):
    # x,y 일반적인 변수타입
    # *z, 가변 인수
    # 언패킹 : 여러개의 값을 각각의 변수에 나눠 담는 과정
    # 자바스크립트에서 디스트럭쳐링(destructuring)

    x, y, *z = args
    return x, y, z


print(b(1, 2, 3, 4, 5))
