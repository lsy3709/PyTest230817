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
Oh, I believe in yesterday
"
'''.lower().split()

word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1

test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t: t[1],
                                      reverse=True)).items()
# print(f"test_OrderedDict 의 결괏값 전체: {test_OrderedDict}")

count = 0
for word, freq in test_OrderedDict:
    if count < 10:
        print(f"단어 {word}, 빈도 : {freq}")
        count += 1
    else :
        break


