from collections import OrderedDict

d = OrderedDict()
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6

# 값에 따라 정렬
sorted_d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

for k, v in sorted_d.items():
    print(f"key: {k}, value: {v}")
