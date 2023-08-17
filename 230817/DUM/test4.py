
# 거꾸로 말하기

print("거꾸로 말할 문장 :")
sentence = input()
reverse_sentence = ''
print("거꾸로 말하면 :")
for char in sentence:
    reverse_sentence = char + reverse_sentence
print(reverse_sentence)