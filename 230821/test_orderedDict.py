from collections import OrderedDict
# 기본 딕션너리
# d = {}
# 정렬된 딕션너리,
# collections 모듈에서, OrderedDict 클래스 이용해서.

# 정렬 옵션 함수 추가 및, sorted 함수 이용하기.


# t[0] : key, t[1]: value
def sort_by_key(t):
    return t[0]


def sort_by_value(t):
    return t[1]


d = dict()
d['b'] = 10
d['a'] = 2
d['d'] = 7
d['c'] = 6

test_OrderedDict = OrderedDict(sorted(d.items(), key=sort_by_key)).items()

# for k, v in d.items():
#     print(f" key : {k}, value: {v}")

for k, v in test_OrderedDict:
    print(f" key : {k}, value: {v}")
