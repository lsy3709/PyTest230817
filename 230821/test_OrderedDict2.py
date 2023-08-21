from collections import OrderedDict
# 기본 딕션너리
# d = {}
# 정렬된 딕션너리,
# collections 모듈에서, OrderedDict 클래스 이용해서.

# 정렬 옵션 함수 추가 및, sorted 함수 이용하기.

d = {}
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6

# t[0] : key, t[1]: value
def sort_by_key(t):
    return t[0]

for k, v in d.items():
    print(f"key: {k}, value: {v}")

print("\n")
d = OrderedDict()
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6
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
# 값에 따라 정렬
sorted_dict = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
for k, v in sorted_dict.items():
    print(f"key: {k}, value: {v}")
print("\n")
sorted_dict = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
for k, v in sorted_dict.items():
    print(f"key: {k}, value: {v}")
