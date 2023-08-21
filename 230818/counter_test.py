from collections import Counter as ct

text = list("apple")

print(f"text 출력: {text}")

# Counter라는 클래스를 ct로 줄여서 표현
# 웰노움 클래스들은 정해진 이름들이 있음. 예) numpy->np, pandas->pd
c = ct(text)
print(f"Counter의 결과 집계하여 키와 값으로표현: {c}")
