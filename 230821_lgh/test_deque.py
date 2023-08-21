from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(f"deque_list의 출력 : {deque_list}")

# for i in range(5):
#     deque_list.appendleft(i)
# print(f"deque_list appenleft의 출력 : {deque_list}")

# print(f"해당 deque의 요소의 메모리 위치 주소 값 : id(deque_list[0]) : {id(deque_list[0])}")

# deque_list.rotate(2)
# print(f"test_deque_rotate의 출력 : {deque_list}")
# print(f"해당 deque의 요소의 메모리 위치 주소 값 : id(deque_list[2]) : {id(deque_list[2])}")

# test_deque_reverse = deque(reversed(deque_list))
# print(f"test_deque_reverse의 출력 : {test_deque_reverse}")

deque_list.extend([5, 6, 7])
print(f"deque_list extend([5, 6, 7])의 출력 : {deque_list}")

deque_list.extendleft([8, 9, 10])
print(f"deque_list extendleft([8, 9, 10])의 출력 : {deque_list}")