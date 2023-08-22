from collections import OrderedDict

# 기본 딕셔너리
# d = {}

# 정렬 된 딕셔너리, collections 모듈에서, OrderDict 클래서 이용

# 정렬 옵션 함수 추가 및, sorted 함수 이용하기.

# t[0] : key, t[1]: value
def sort_by_key(t):
    return t[0]

def sort_by_value(t):
    return t[1]

d = OrderedDict()
d['b'] = 10
d['a'] = 1
d['d'] = 5
d['c'] = 2

test_OrderedDict = OrderedDict(sorted(d.items(), key=sort_by_key)).items()

# for k, v in d.items():
#     print(f"key : {k}, value : {v}")

for k, v in test_OrderedDict:
    print(f"key : {k}, value : {v}")