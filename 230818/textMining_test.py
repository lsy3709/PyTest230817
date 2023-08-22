# defaultdict는 값이 없는 경우 지정된 디폴트 값으로 대체/ OrderedDict는 정렬을 도와주는 도구
from collections import defaultdict, OrderedDict

text = '''
"Yesterday all my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly.
Why she had to go I don't know,
she wouldn't say.
I said something wrong
now I long for yesterday.
Yesterday love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she had to go I don't know
she wouldn't say
I said something wrong
now I long for yesterday
Yesterday love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday."
'''.lower().split()

word_count = defaultdict(lambda: 0)
print(f"결과값 전체:  {text}")
for word in text:
    word_count[word] += 1

for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(f"결과값: i: {i}, v: {v}")
