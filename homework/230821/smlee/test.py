# test_230818 We are young

f = open("\PyTest2023\PyTest230817\homework/smlee/We_are_young.txt",
         'r', encoding='utf-8')
young_lyric = f.readlines()
print(young_lyric)
f.close()

contents = ""
for line in young_lyric:
    contents = contents + line.strip() + "\n"
    result = contents.upper().count("WE")
    print(f"가사 중 we를 대문자로 변환한 갯수를 찾은 결과 값: {result}" + "\n")
    print(f"contents의 내용: {contents}")
