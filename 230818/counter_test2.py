from collections import Counter

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
Oh, I believe in yesterday"
'''.lower().split()
# .lower 소문자로 바꾸고 .split 나누기
print(f"text 결과값: {text}")
print("\n")
print(f"Counter모듈 이용출력: {Counter(text)}")
