# defaultdict : 값이 없는 경우 지정된 디폴트 값으로 대체
# OrderedDict : 정렬을 쉽게 도와주는 도구
from collections import defaultdict, OrderedDict

# 순서, 작은 따옴표 3개
# 그 안에 큰 따옴표 안에
# 해당 가사 또는 기사, 또는 문장을 넣기
# lower -> 소문자로 모두 변환, split -> 기본이 공백을 기준으로, 단어를 분리하기
# 결과를 text라는 변수에, 리스트 형식으로 담기
text = '''
"Yesterday all my troubles
seemed so far away
Now it looks as though
they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go
I don't know, she wouldn't say
I said something wrong
now I long for yesterday
Yesterday love was such an
easy game to play
Now I need a place to hide away
Oh, I believe in yesterday.
Why she had to go
I don't know, She wouldn't say
I said something wrong
Now I long for yesterday
Yesterday love was
such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
"
'''.lower().split()

# defaultdict -> 값이 없으면 기본값을 0으로 지정
# lambda 매개변수 : 수행하는 문장(리턴)
# 타입 : 딕셔너리, 키 : 값의 구조 형태
word_count = defaultdict(lambda : 0)

# yesterday의 가사 내용이고, 리스트에서 구분된 단어들을 하나씩 꺼내어서 word 담아서 작업할 예정
# { 'a' : 2, }
# word 단어의 빈도를 집계(숫자 세기)
for word in text :
    word_count[word] += 1

# OrderedDict 이용해서 정렬
# OrderedDict(매개변수1(정렬된 딕셔너리)).items -> 키, 값을 둘다 가져오는 구조
# sorted(매개변수1(집계된 딕셔너리 키와 값), 매개변수2(정렬기준 : 람다식), 매개변수3(기본 오름차순, reverse=True 내림차순))
# lambda t:t[1] -> t : 매개변수(튜플 형식), t[1] : 결과 값(value)
test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t:t[1],
                                      reverse=True)).items()
print(f"test_OrderedDict의 결과 값 전체 : {test_OrderedDict}")
for i, v in test_OrderedDict :
    print(f"test_OrderedDict의 결과 값 요소 : i : {i}, v : {v}")