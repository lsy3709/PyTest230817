from collections import OrderedDict

d = {}
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6

for k, v in d.items():
    print(f"key: {k}, value: {v}")

print("\n")
d = OrderedDict()
d['a'] = 10
d['b'] = 2
d['c'] = 7
d['d'] = 6

# 값에 따라 정렬
sorted_dict = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
for k, v in sorted_dict.items():
    print(f"key: {k}, value: {v}")
print("\n")
sorted_dict = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
for k, v in sorted_dict.items():
    print(f"key: {k}, value: {v}")
