test_dict = {"a": 1, "b": 2, "c": 3}
print(f"test_dict 출력 : {test_dict}")

test_keys = test_dict.keys()
print(f"test_keys 출력: {test_keys}")

test_values = test_dict.values()
print(f"test_values 출력: {test_values}")

test_items = test_dict.items()
print(f"test_items 출력: {test_items}")

for k, v in test_items:
    print(f"test_tiems: {k}:{v}")

for key, value in test_dict.items():
    print(key, value)

# 예제2
my_dict = {}
my_dict['name'] = ['Angel', 'Lisa', 'Kevin']
my_dict['age'] = [30, 43, 15]

print(my_dict['name'])
for key, value in my_dict.items():
    print(key, value)
