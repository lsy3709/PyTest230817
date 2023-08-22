f = open("./homework/230818/230818_lys/yesterday.txt", 'r', encoding='utf-8')

yesterday_lyric = f.readlines()

print(f"yesterday_lyric의 내용 출력 부분 : {yesterday_lyric}")

f.close()

contents = ""

for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

print(f"contents의 내용이 궁금 하면 반복문 다 종료후 : {contents}")

result = contents.upper().count("YESTERDAY")

print(f"가사 중에 yesterday 를 대문자로 변환 후 갯수 찾은 결과: {result}")
