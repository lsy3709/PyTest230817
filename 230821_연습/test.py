from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(f"deque_list의 출력: {deque_list}")

# .appendleft
deque_list01 = deque()
for i in range(5):
    deque_list01.appendleft(i)
print(f"deque_list의 출력: {deque_list01}")

# 주소값 확인
print(f"해당 deque 요소의 메모리 위치 주소값: id(deque_list[0]) : {id(deque_list[0])}")

# rotate
deque_list.rotate(2)
print(f"test_deque_rotate의 출력: {deque_list}")
# test_deque_rotate의 출력: deque([3, 4, 0, 1, 2])
# 로테이트 후 인덱스 주소값
print(f"해당 deque 요소의 메모리 위치 주소값: id(deque_list[0]) : {id(deque_list[2])}")

# reversed
print(deque(reversed(deque_list)))
# deque([3, 4, 0, 1, 2]) -> deque([2, 1, 0, 4, 3])


# extend(), extendleft()
deque_list01.extend([5, 6, 7])
print(f"test_deque_extend의 출력: {deque_list01}")

deque_list01.extendleft([8, 9, 10])
print(f"test_deque_extendleft의 출력: {deque_list01}")
