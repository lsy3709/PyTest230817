# vscode에서 기본 실행 단추키 , ctrl + f5
# 순서 : 이해가 안되는 코드의 줄번호 앞에 클릭해서 중단점 설정
# 디버깅 할 때는 f5
# 컨트롤러 창 -> 1) step into, 2) step over, 3)


# input() : 터미널에서 , 문자열을 입력하는 형식.
print("이메일을 입력해주세요 ")
email = input()
print(f"입력된 이메일은 : {email}")


print("hello python")
# ctrl + f5
a = 1
print(type(a))
b = str(a)
print(b)
print(type(b))
# 출력 형식, f 포맷 스트링 .
print(f"test a출력: {a}")
# 코틀린 로그캣 출력.
# Log.d("lsy","출력하기 a : ${a}")

print("출력형식 %d " % (a))
