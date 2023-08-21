# collections 모듈안에 여러 클래스 중에 하나만 선택 해서 사용
# 별칭, 또는 단축키 처럼 Counter => ct 축약해서 사용 가능
from collections import Counter as ct

# apple 문자열 => list 함수를 이용해서, 리스트 타입으로 변환
text = list("apple")
print(f"text 출력 : {text}")

# Counter 라는 클래스를 ct로 줄여서 표현했고, 줄이는 단어는 편한대로 사용하면 됨
# 웰노움 클래스들은 정해진 이름들이 있음
# 예) numpy -> np, pandas -> pd
c = ct(text)
print(f"Counter의 결과, 집계 키와 값의 구조로 표현 : {c}")