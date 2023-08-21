test_dict = {"a": 1, "b": 2, "c": 3}
print(f"test_dict 출력 : {test_dict}")

test_keys = test_dict.keys()
print(f"test_keys 출력 : {test_keys}")

test_values = test_dict.values()
print(f"test_values 출력 : {test_values}")

test_items = test_dict.items()
print(f"test_items 출력 : {test_items}")

for k, v in test_items:
    print(f"key 값: {k}, value 값 : {v}")
