# vscode에서, 기본 실행 단축키, ctrl + f5
# 순서는, 이해가 안되는 코드의 줄번호 앞에 클릭, 중단점 설정.
# 디버깅 할 때는, f5 누르면 됨.
# 컨트롤러 창 -> 1) step into , 2) step over, 3)


sen = "I love you"
reverse = ' '
for char in sen:
    reverse = char + reverse
    print(reverse)
print(reverse)

# import sys
# print(sys.getsizeof("a"))

# def test(**arg):
#     x, y, z = arg
#     return x, y, z


# print(test(f=3, s=2, t=6))

# def spam(eggs):
#     print(f"eggs id 순서2-1: {id(eggs)}")
#     eggs.append(1)
#     print(f"eggs id 순서2-2: {id(eggs)}")
#     eggs = [2, 3]
#     print(f"eggs id 순서2-3: {id(eggs)}")
#     print(eggs)
#     print(f"eggs id 순서2-4: {id(eggs)}")


# ham = [0]
# print(f"ham의 id 순서1 : {id(ham)}")
# spam(ham)
# print(ham)
# print(f"ham의 id 순서3: {id(ham)}")

# def f(x):
#     y = x
#     x = 5
#     return y * y

# x = 3
# print(f(x))
# print(x)
