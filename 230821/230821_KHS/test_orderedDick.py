from collections import OrderedDict

#기본 딕셔너리
# d = {}

#정렬된 딕셔너리
#collections 모듈에서, OrderedDict 클래스 이용해서
#정렬함수

def sort_by_value(t):
    return : t[0]
    

d= OrderedDict()

d['a'] = 10
d['b'] = 6
d['c'] = 2
d['d'] = 7

test_OrderedDict = OrderedDict(sorted(d.items(), key=sort_by_value)).items
for k, v in d.items():
    print(f"key : {k}, value: {v}")

for k, v in test_OrderedDict():
    print(f"key : {k}, value: {v}")
