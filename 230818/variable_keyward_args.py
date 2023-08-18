# 키워드 가변 인자 -> ** 를 사용해서 정의하면 됨.
def c(**kwargs):
    print(kwargs)


# 호출하는 부분 확인. -> json -> "a" : "b"
# 호출 구분자, = .
c(f=1, s=2)
